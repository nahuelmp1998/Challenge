from fastapi import APIRouter
from config.database import get_session
from model.character import Character

router = APIRouter()


@router.get("/character/getAll")
def get_all_characters():
    session = get_session()
    characters = session.query(Character).all()
    print("Personajes: ", characters)
    return characters
