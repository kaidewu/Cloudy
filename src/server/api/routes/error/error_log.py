from uuid import uuid4
from datetime import datetime
from database.connection import engine
from database import models
from sqlalchemy.orm import sessionmaker

# Get connection to the MySQL Database
Session = sessionmaker(bind=engine)
session = Session()

class Error:
    def __init__(
            self,
            error_traceback: str,
            error_massage: str,
            status: int,
            endpoint: str
            ) -> None:
        self.error_uuid = str(uuid4())
        self.error_register_at = datetime.now()
        self.error_status = status
        self.error_endpoint = endpoint
        self.error_traceback = error_traceback
        self.error_massage = error_massage

    def insert_error_db(self):

        '''
            Insert into table LOGS
        '''

        insert_query_logs = models.Logs(
            LOG_UUID = self.error_uuid,
            LOG_REGISTER_AT = self.error_register_at,
            LOG_LEVEL = 2 if (self.error_status >= 500) and (self.error_status <= 509) else 1,
            LOG_BODY = self.error_traceback,
            LOG_USER_ID = 1,
            LOG_ENDPOINT = self.error_endpoint,
            LOG_DELETED = 0,
            LOG_DELETED_DATE = None
        )

        session.add(insert_query_logs)
        session.commit()
        session.refresh(insert_query_logs)

        return {
                "status": self.error_status,
                "errorId": self.error_uuid,
                "errorLevel": "Internal Error" if (self.error_status >= 500) and (self.error_status <= 509) else "Warning",
                "errorMessage": self.error_massage
            }
