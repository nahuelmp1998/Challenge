from fastapi import FastAPI
from config.lifespan import lifespan
from controllers.character_controller import router as character_router

app = FastAPI(lifespan=lifespan)
app.include_router(character_router) 
