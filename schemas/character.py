from pydantic import BaseModel, Field
''' 
    Documentation: 
        -https://docs.pydantic.dev/latest/concepts/models/#rebuilding-model-schema
        -https://docs.pydantic.dev/1.10/usage/models/
        -https://fastapi.tiangolo.com/tutorial/response-model/#add-an-output-model
'''

class CharacterModel(BaseModel):
    id: int = Field(..., description="Unique identifier of the character")
    name: str = Field(..., min_length=1, description="Name of the character")
    height: int = Field(..., description="Height in cm")
    mass: int = Field(..., description="Mass in kg")
    eye_color: str = Field(..., description="Eye color of the character")
    birth_year: int = Field(..., gt=0, description="Birth year of the character")
    
    class Config:
        orm_mode = True
        
    
class CharacterDetailedModel(CharacterModel):
    hair_color: str = Field(..., description="Hair color of the character")
    skin_color: str = Field(..., description="Skin color of the character")
   
    class Config:
        orm_mode = True
            
         