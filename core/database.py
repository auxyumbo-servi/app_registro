from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

BASE_DIR = Path(__file__).parent

DB_PATH = BASE_DIR / "testing.db"

DB_PATH.parent.mkdir(exist_ok=True)

DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(DATABASE_URL,
                        echo=True)

SessionLocal = sessionmaker(bind=engine,
                            autoflush=False,
                            autocommit=False)

class Base (DeclarativeBase):
    pass

def create_tables():
    Base.metadata.create_all(engine)

def get_session():
    return SessionLocal()