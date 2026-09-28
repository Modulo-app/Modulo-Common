from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

def make_session_factory(database_url: str) -> sessionmaker[Session]:
    engine = create_engine(database_url)
    return sessionmaker(bind=engine, autoflush=False)
