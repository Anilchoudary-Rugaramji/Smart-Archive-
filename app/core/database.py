from sqlalchemy import engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings


engine = engine.create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=True, autocommit=False)
Base = declarative_base()
