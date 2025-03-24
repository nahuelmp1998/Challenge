from contextlib import asynccontextmanager
from fastapi import FastAPI
from config.database import init_db, close_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creando base de datos...")
    init_db()
    yield
    print("Chau")

