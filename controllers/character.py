from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from config.database import get_session
from schemas.character import CharacterModel, CharacterDetailedModel
from services.character_service import CharacterService


router = APIRouter()


def get_session_on_service(session=Depends(get_session)):
    return CharacterService(session)


@router.get(
    "/character/getAll", tags=["Characters"], response_model=list[CharacterModel]
)
def get_all_characters(
    service: CharacterService = Depends(get_session_on_service),
) -> list[CharacterModel]:
    characters = service.get_all_characters()
    return characters


@router.get(
    "/character/get/{id}", tags=["Characters"], response_model=CharacterDetailedModel
)
def get_character_by_id(
    id: int, service: CharacterService = Depends(get_session_on_service)
) -> CharacterDetailedModel | JSONResponse:
    character = service.get_character_by_id(id)
    return character


@router.post(
    "/character/add", tags=["Characters"], response_model=CharacterDetailedModel
)
def add_new_character(
    character: CharacterDetailedModel,
    service: CharacterService = Depends(get_session_on_service),
) -> JSONResponse:
    response = service.add_new_character(character)
    return response


@router.delete("/character/delete/{id}", tags=["Characters"])
def delete_character(
    id: int, service: CharacterService = Depends(get_session_on_service)
) -> JSONResponse:
    response = service.delete_character(id)
    return response
