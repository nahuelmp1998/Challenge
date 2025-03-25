from fastapi import APIRouter
from config.database import get_session
from model.character import Character

router = APIRouter()


@router.get("/character/getAll", tags=["Characters"])
def get_all_characters():
    session = get_session()
    characters = session.query(Character).all()
    requested_attributes = ["id", "name", "height", "mass", "birth_year", "eye_color"]
    characters_formatted = [{attr: getattr(char, attr)} for char in characters for attr in requested_attributes]
    return characters_formatted

@router.get("/character/get/{id}", tags=["Characters"])
def get_character_by_id(id: int):
    session = get_session()
    character = session.query(Character).filter(Character.id == id).first()
    return character
    

