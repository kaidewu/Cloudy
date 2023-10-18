import os
import sys
sys.path[0] = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

from sqlalchemy import create_engine, text
from test_constants import MYSQL_URL

def test_validate_if_exists_users():
    try:
        engine = create_engine(MYSQL_URL)
        with engine.connect() as connection:
            connection.execute(text("SELECT 1 FROM USERS")).first()
    except:
        raise Exception(sys.exc_info())