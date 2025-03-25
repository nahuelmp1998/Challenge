"""
Documentation used
    -https://docs.sqlalchemy.org/en/20/orm/quickstart.html#declare-models
"""

from fastapi import FastAPI
from config.lifespan import lifespan
from controller.character import router as character_router

app = FastAPI(lifespan=lifespan)
app.include_router(character_router)  # Aquí lo incluyes


@app.get("/")
def home():
    return "Challenge with MVC Desing Pattern"
