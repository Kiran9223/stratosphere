from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Create a new database
DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/stratosphere"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()