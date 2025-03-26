"""
Documentation used
    -https://docs.sqlalchemy.org/en/20/orm/quickstart.html#declare-models
    -https://docs.sqlalchemy.org/en/20/tutorial/data_update.html
"""

from fastapi import FastAPI
from config.lifespan import lifespan
from controller.character import router as character_router

app = FastAPI(lifespan=lifespan)
app.include_router(character_router)  # Aquí lo incluyes
