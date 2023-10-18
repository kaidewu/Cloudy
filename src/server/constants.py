import os
from dotenv import dotenv_values

# ENV Path
ENV_DIR = f"{os.path.abspath(os.path.dirname(__file__))}/.env"
# Load ENV file
ENV_VARS = dotenv_values(ENV_DIR)

# Time format
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S.%M"