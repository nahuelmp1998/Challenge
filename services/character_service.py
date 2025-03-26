from fastapi.responses import JSONResponse
from sqlalchemy.orm import sessionmaker, Session
from schemas.character import CharacterModel, CharacterDetailedModel
from models.character import CharacterSQL


class CharacterService:
    def __init__(self, session: Session):
        self.session = session

    def get_all_characters(self) -> list[CharacterModel]:
        character = self.session.query(CharacterSQL).all()
        self.session.close()
        return character

    def get_character_by_id(self, id) -> CharacterDetailedModel | JSONResponse:
        character = (
            self.session.query(CharacterSQL).filter(CharacterSQL.id == id).first()
        )
        if character is None:
            return JSONResponse(
                status_code=404, content={"message": "Character not found"}
            )
        self.session.close()
        return character

    def add_new_character(self, character: CharacterDetailedModel) -> JSONResponse:
        # Adding a new character if it does not already exist
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
            self.session.query(CharacterSQL)
            .filter(CharacterSQL.id == character_sql.id)
            .first()
        )
        if result:
            return JSONResponse(
                status_code=404,
                content={
                    "message": f"Character already exists with id: {character_sql.id}"
                },
            )
        else:
            self.session.add(character_sql)
            self.session.commit()
            return JSONResponse(
                status_code=200, content={"message": "Character added succesfully"}
            )
            
    def delete_character(self, id: int) -> JSONResponse:
            # Deleting character if it does not already exist
            try:
                character = (
                    self.session.query(CharacterSQL).filter(CharacterSQL.id == id).first()
                )
                if not character:
                    return JSONResponse(
                        status_code=404, content={"message": "Character not found"}
                    )
                self.session.delete(character)
                self.session.commit()
                return JSONResponse(
                    status_code=200, content={"message": "Character deleted"}
                )
            except Exception:
                return JSONResponse(
                    status_code=500,
                    content={"message": "Internal Server Error with database"},
                )
