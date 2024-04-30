from sqlmodel import SQLModel, create_engine

from app.config.config import settings

if settings.DB_URI:
    engine = create_engine(settings.DB_URI)


def init_db():
    if engine:
        SQLModel.metadata.create_all(engine)
