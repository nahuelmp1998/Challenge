from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models.character import CharacterSQL
from models.base import Base


engine = create_engine("sqlite:///./characters.db", echo=True)
Session = sessionmaker(engine)


def init_db():
    '''Initialize the database and add a new character if it is empty'''
    
    Base.metadata.create_all(engine)
    session = Session()
    
    if session.query(CharacterSQL).count() == 0:
        add_new_character(session)
    return


def get_session():
    return Session()


def add_new_character(session: Session):
    '''Add the new character if it does not already exist'''
    
    characters = [
        CharacterSQL(
            id=1,
            name="Luke Skywalker",
            height=172,
            mass=77,
            hair_color="blond",
            skin_color="fair",
            eye_color="blue",
            birth_year=1998,
        ),
    ]

    session.add_all(characters)
    session.commit()
