from pydantic import BaseModel, Field


class CharacterModel(BaseModel):
    id: int = Field(..., description="Unique identifier of the character")
    name: str = Field(..., min_length=1, description="Name of the character")
    height: int = Field(..., description="")
    mass: int = Field(..., description="")
    eye_color: str = Field(..., description="Eye color of the character")
    birth_year: int = Field(..., gt=0, description="Birth year of the character")
    
    class Config:
        orm_mode = True
        
    
class CharacterDetailedModel(CharacterModel):
    hair_color: str = Field(..., description="Hair color of the character")
    skin_color: str = Field(..., description="Skin color of the character")
   
    class Config:
        orm_mode = True
            
         
