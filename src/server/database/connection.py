from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values
import os

env_vars = dotenv_values(f"{os.path.dirname(os.path.dirname(__file__))}/.env")

MYSQL_URL = f"mysql+mysqlconnector://{env_vars['MYSQL_USERNAME']}:{env_vars['MYSQL_PASSWORD']}@{env_vars['MYSQL_HOST']}/{env_vars['MYSQL_DATABASE']}"# f"mysql+mysqlconnector://{os.getenv('MYSQL_USERNAME')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DATABASE')}"

# Create database engine and session
engine = create_engine(MYSQL_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)