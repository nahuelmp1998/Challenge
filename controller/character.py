from fastapi import APIRouter
from config.database import get_session
from model.character import Character

router = APIRouter()


@router.get("/character/getAll")
def get_all_characters():
    session = get_session()
    characters = session.query(Character).all()
    requested_attributes = ["id", "name", "height", "mass", "birth_year", "eye_color"]
    characters_formatted = [{attr: getattr(char, attr)} for char in characters for attr in requested_attributes]
    return characters_formatted
