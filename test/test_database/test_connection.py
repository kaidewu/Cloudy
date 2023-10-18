import os
import sys
sys.path[0] = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

from sqlalchemy import create_engine
from test_constants import MYSQL_URL

def test_connection_to_the_database_server():
    try:
        engine = create_engine(MYSQL_URL)
        engine.connect()
    except:
        raise Exception(sys.exc_info())