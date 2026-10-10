from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:#sp1234@localhost:5432/smart_civic"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

try:
    with engine.connect() as connection:
        print("PostgreSQL connected successfully!")
except Exception as e:
    print("Database connection failed:")
    print(e)