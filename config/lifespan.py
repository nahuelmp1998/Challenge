from contextlib import asynccontextmanager
from fastapi import FastAPI
from config.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    """It load and initialize the database"""
    init_db()
    yield
