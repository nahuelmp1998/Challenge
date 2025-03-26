from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from model.base import Base
from pydantic import BaseModel, Field


class CharacterSQL(Base):
    __tablename__ = "Character"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    height: Mapped[int]
    mass: Mapped[int]
    hair_color: Mapped[str] = mapped_column(String(30))
    skin_color: Mapped[str] = mapped_column(String(30))
    eye_color: Mapped[str] = mapped_column(String(30))
    birth_year: Mapped[int]
    
    def __repr__(self):
        return f"Character(id={self.id}, name={self.name}, height={self.height}, mass={self.mass})"


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
            
         