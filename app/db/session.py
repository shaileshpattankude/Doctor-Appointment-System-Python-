from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from app.core.config import settings

DATABASE_URL = settings.DATABASE_URL
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db() -> Generator[Session]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
