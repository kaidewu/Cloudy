from fastapi import APIRouter, Depends, status

from sqlalchemy import and_, or_
from sqlalchemy.orm import Session
from database.connection import SessionLocal
from database import models
from api.routes.error.error_log import Error

import traceback
from datetime import datetime

error_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@error_router.get("/logs", summary="Get logs of the application. Warnings or Errors")
async def get_logs(
    errorId: str = None,
    startDate: int = None,
    endDate: int = None,
    db: Session = Depends(get_db)
):
    results = {}

    try:
        all_logs = []

        query = db.query(
            models.Logs.LOG_UUID,
            models.Logs.LOG_REGISTER_AT,
            models.Logs.LOG_BODY,
            models.Logs.LOG_ENDPOINT,
            models.LogLevels.LOG_LEVEL_TYPE_NAME
        ).join(models.LogLevels, models.Logs.LOG_LEVEL == models.LogLevels.LOG_LEVEL_TYPE_ID)

        # Dynamic filters based on conditions
        filters = [
            models.Logs.LOG_DELETED == False,
            models.LogLevels.LOG_LEVEL_TYPE_DELETED == False
        ]

        if startDate is not None:
            filters.append(models.Logs.LOG_REGISTER_AT >= startDate)

        if endDate is not None:
            filters.append(models.Logs.LOG_REGISTER_AT <= endDate)

        if errorId is not None and errorId != "":
            filters.append(models.Logs.LOG_UUID == errorId)

        # Apply filters to the query using the and_ function to combine multiple filters with AND
        get_logs = query.filter(and_(*filters))

        if (get_logs is None) or (get_logs == []) or (get_logs == "null"):
            results.update(Error(
                f"{errorId} not exists" if (errorId is not None) or (errorId != "") else "Not register Logs yet",
                f"{errorId} not exists" if (errorId is not None) or (errorId != "") else "Not register Logs yet",
                status.HTTP_400_BAD_REQUEST,
                "http://192.168.1.47/api/v1/logs"
            ).insert_error_db())

            return results
        
        for log in get_logs:
            all_logs.append({
                "logId": log[0],
                "logRegisterAt": datetime.fromtimestamp(log[1]).isoformat(),
                "logTitle": str(log[2]).splitlines()[-1],
                "logBody": log[2],
                "logEndpoint": log[3],
                "logLevel": log[4]
            })

        return {
            "status": status.HTTP_200_OK,
            "logs": all_logs
        }
        
    except:
        results.update(Error(
                traceback.format_exc(),
                traceback.format_exc().splitlines()[-1],
                status.HTTP_500_INTERNAL_SERVER_ERROR,
                "http://192.168.1.47/api/v1/logs"
            ).insert_error_db())