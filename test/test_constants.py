import os
from dotenv import dotenv_values

# ENV Path
TEST_ENV_DIR = f"{os.path.abspath(os.path.dirname(__file__))}/.env.test"
# Load ENV file
TEST_ENV_VARS = dotenv_values(TEST_ENV_DIR)

# Time format
TEST_DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S.%M"

#MySQL URL
MYSQL_URL = f"mysql+mysqlconnector://{TEST_ENV_VARS['TEST_MYSQL_USERNAME']}:{TEST_ENV_VARS['TEST_MYSQL_PASSWORD']}@{TEST_ENV_VARS['TEST_MYSQL_HOST']}/{TEST_ENV_VARS['TEST_MYSQL_DATABASE']}"
