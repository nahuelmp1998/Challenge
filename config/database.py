from sqlalchemy import create_engine
from model.character import Character
from model.base import Base

''' 
    https://docs.sqlalchemy.org/en/20/core/connections.html
    
    El garbage collector de python se encarga de cerrar la conexión cuando detecta
    que no está más en uso.
    
    Para un manejo más claro de las conexiones es mejor utilizar instancias de Session.
'''

engine = create_engine("sqlite:///./characters.db", echo=True)

def init_db():
    Base.metadata.create_all(engine)
    