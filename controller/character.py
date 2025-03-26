from fastapi import APIRouter
from fastapi.responses import JSONResponse
from config.database import get_session
from model.character import CharacterSQL, CharacterModel, CharacterDetailedModel

router = APIRouter()


@router.get(
    "/character/getAll", tags=["Characters"], response_model=list[CharacterModel]
)
def get_all_characters() -> CharacterModel:
    with get_session() as session:
        characters = session.query(CharacterSQL).all()
        return characters


@router.get(
    "/character/get/{id}", tags=["Characters"], response_model=CharacterDetailedModel
)
def get_character_by_id(id: int):
    with get_session() as session:
        character = session.query(CharacterSQL).filter(CharacterSQL.id == id).first()
        if character is None:
            return JSONResponse(
                status_code=404, content={"message": "Character not found"}
            )
        return character


@router.post("/character/add", tags=["Characters"])
async def add_new_character(character: CharacterDetailedModel):
    with get_session() as session:
        # character_sql = CharacterSQL(**({key: value} for key, value in character.__dict__.items())) #Genero un diccionario con los valores de character y lo mapeo al modelo Sql, NO SE PORQ NO FUNCIONA XD
        character_sql = CharacterSQL(
            id=character.id,
            name=character.name,
            height=character.height,
            mass=character.mass,
            hair_color=character.hair_color,
            skin_color=character.skin_color,
            eye_color=character.eye_color,
            birth_year=character.birth_year,
        )
        result = (
            session.query(CharacterSQL).filter(CharacterSQL.id == character.id).first()
        )
        if result:
            return JSONResponse(
                status_code=404,
                content={"message": "Character already exists with id: {character.id}"},
            )
        else:
            session.add(character_sql)
            session.commit()
            return JSONResponse(
                status_code=200, content={"message": "Character added succesfully"}
            )


@router.delete("/character/delete/{id}", tags=["Characters"])
def delete_character(id: int):
    with get_session() as session:
        try:
            character = (
                session.query(CharacterSQL).filter(CharacterSQL.id == id).first()
            )
            if not character:
                return JSONResponse(
                    status_code=404, content={"message": "Character not found"}
                )
            session.delete(character)
            session.commit()
            return JSONResponse(
                status_code=200, content={"message": "Character deleted"}
            )
        except Exception as e:
            return JSONResponse(
                status_code=500,
                content={"message": "Internal Server Error with database"},
            )
