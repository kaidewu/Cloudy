from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from constants import ENV_VARS

MYSQL_URL = f"mysql+mysqlconnector://{ENV_VARS['MYSQL_USERNAME']}:{ENV_VARS['MYSQL_PASSWORD']}@{ENV_VARS['MYSQL_HOST']}/{ENV_VARS['MYSQL_DATABASE']}"# f"mysql+mysqlconnector://{os.getenv('MYSQL_USERNAME')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DATABASE')}"

# Create database engine and session
engine = create_engine(MYSQL_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)