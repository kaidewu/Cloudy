import os
import sys
sys.path[0] = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

from sqlalchemy import create_engine, inspect
from test_constants import MYSQL_URL
from test_database import test_models as models

def test_validate_if_exists_users():
    try:
        engine = create_engine(MYSQL_URL)
        inspector = inspect(engine)
        assert inspector.has_table(models.User.__tablename__) == True
    except:
        raise Exception(sys.exc_info())
    
def test_validate_if_exists_logs():
    try:
        engine = create_engine(MYSQL_URL)
        inspector = inspect(engine)
        assert inspector.has_table(models.Logs.__tablename__) == True
    except:
        raise Exception(sys.exc_info())
    
def test_validate_if_exists_logs_levels():
    try:
        engine = create_engine(MYSQL_URL)
        inspector = inspect(engine)
        assert inspector.has_table(models.LogLevels.__tablename__) == True
    except:
        raise Exception(sys.exc_info())
    
def test_validate_if_exists_account():
    try:
        engine = create_engine(MYSQL_URL)
        inspector = inspect(engine)
        assert inspector.has_table(models.Account.__tablename__) == True
    except:
        raise Exception(sys.exc_info())
    
def test_validate_if_exists_account_types():
    try:
        engine = create_engine(MYSQL_URL)
        inspector = inspect(engine)
        assert inspector.has_table(models.AccountCurrencyType.__tablename__) == True
    except:
        raise Exception(sys.exc_info())
    
def test_validate_if_exists_categories():
    try:
        engine = create_engine(MYSQL_URL)
        inspector = inspect(engine)
        assert inspector.has_table(models.Categories.__tablename__) == True
    except:
        raise Exception(sys.exc_info())
    
def test_validate_if_exists_category_icons():
    try:
        engine = create_engine(MYSQL_URL)
        inspector = inspect(engine)
        assert inspector.has_table(models.CategoryIcons.__tablename__) == True
    except:
        raise Exception(sys.exc_info())
    
def test_validate_if_exists_subcategories():
    try:
        engine = create_engine(MYSQL_URL)
        inspector = inspect(engine)
        assert inspector.has_table(models.SubCategories.__tablename__) == True
    except:
        raise Exception(sys.exc_info())
    
def test_validate_if_exists_relation_categories():
    try:
        engine = create_engine(MYSQL_URL)
        inspector = inspect(engine)
        assert inspector.has_table(models.RelationCategories.__tablename__) == True
    except:
        raise Exception(sys.exc_info())
    
def test_validate_if_exists_wallet():
    try:
        engine = create_engine(MYSQL_URL)
        inspector = inspect(engine)
        assert inspector.has_table(models.Wallets.__tablename__) == True
    except:
        raise Exception(sys.exc_info())