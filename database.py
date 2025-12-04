from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"

# Create engine (connects to DB)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False}
)

# SessionLocal → used to talk to database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base → used to create database tables/models
Base = declarative_base()
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()