from contextlib import asynccontextmanager
from fastapi import FastAPI
from config.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    ''' It load, initialize and create the database'''
    
    init_db()
    
    yield
    
    print("Chau")
