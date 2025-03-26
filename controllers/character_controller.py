from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from config.database import get_session
from schemas.character import CharacterModel, CharacterDetailedModel
from services.character_service import CharacterService


router = APIRouter(prefix="/character", tags=["Characters"])


# Dependency injection to provide the CharacterService instance using the session for database interaction
def get_session_on_service(session=Depends(get_session)):
    return CharacterService(session)


# Get all characters
@router.get("/getAll", response_model=list[CharacterModel])
def get_all_characters(
    service: CharacterService = Depends(get_session_on_service),
) -> list[CharacterModel]:
    """Retrieve all characters from the database."""
    characters = service.get_all_characters()
    return characters


# Get character by id
@router.get(
    "/get/{id}",
    response_model=CharacterDetailedModel,
    responses={
        404: {
            "description": "Character not found",
            "content": {
                "application/json": {"example": {"message": "Character not found"}}
            },
        }
    },
)
def get_character_by_id(
    id: int, service: CharacterService = Depends(get_session_on_service)
) -> CharacterDetailedModel | JSONResponse:
    """Retrieve a character by its ID."""
    character = service.get_character_by_id(id)
    return character


# Post new character
@router.post("/add", response_model=CharacterDetailedModel)
def add_new_character(
    character: CharacterDetailedModel,
    service: CharacterService = Depends(get_session_on_service),
) -> JSONResponse:
    """Add a new character to the database."""
    response = service.add_new_character(character)
    return response


# Delete a character
@router.delete(
    "/delete/{id}",
    responses={
        404: {
            "description": "Character not found",
            "content": {
                "application/json": {"example": {"message": "Character not found"}}
            },
        }
    },
)
def delete_character(
    id: int, service: CharacterService = Depends(get_session_on_service)
) -> JSONResponse:
    """Delete a character by its ID."""
    response = service.delete_character(id)
    return response
