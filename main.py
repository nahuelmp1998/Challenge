"""
Documentation used
    -https://docs.sqlalchemy.org/en/20/orm/quickstart.html#declare-models
"""

from fastapi import FastAPI
from config.lifespan import lifespan

app = FastAPI(lifespan=lifespan)


@app.get("/")
def home():
    return "Challenge with MVC Desing Pattern"
