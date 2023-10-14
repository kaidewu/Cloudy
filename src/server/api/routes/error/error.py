from fastapi import APIRouter, Depends, status, HTTPException

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
    startDate: str = None,
    endDate: str = None,
    db: Session = Depends(get_db)
):
    results = {}
    all_logs = []
    filters = []

    try:

        if startDate is not None and startDate != "":
            filters.append(models.Logs.LOG_REGISTER_AT >= startDate)

        if endDate is not None and endDate != "":
            filters.append(models.Logs.LOG_REGISTER_AT <= endDate)

        if errorId is not None and errorId != "":
            filters.append(models.Logs.LOG_UUID == errorId)

        get_logs = db.query(
            models.Logs.LOG_UUID,
            models.Logs.LOG_REGISTER_AT,
            models.Logs.LOG_BODY,
            models.Logs.LOG_ENDPOINT,
            models.LogLevels.LOG_LEVEL_TYPE_NAME
            ).join(models.LogLevels, models.Logs.LOG_LEVEL == models.LogLevels.LOG_LEVEL_TYPE_ID
            ).filter(models.Logs.LOG_DELETED == False, 
                     models.LogLevels.LOG_LEVEL_TYPE_DELETED == False,
                     (and_(*filters))
            ).all()

        if (get_logs is None) or (get_logs == []) or (get_logs == "null"):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND
            )
        
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

    except HTTPException as http_exception:
        if http_exception.status_code == 404:
            results.update(Error(
                f"{errorId} not exists" if (errorId is not None) and (errorId != "") else "Not register Logs yet",
                f"{errorId} not exists" if (errorId is not None) and (errorId != "") else "Not register Logs yet",
                http_exception.status_code,
                "http://192.168.1.47/api/v1/logs"
            ).insert_error_db())
        
        raise HTTPException(
            status_code= http_exception.status_code,
            detail=results
        )
    
    except Exception as exception:
        results.update(Error(
                traceback.format_exc(),
                str(exception),
                status.HTTP_500_INTERNAL_SERVER_ERROR,
                "http://192.168.1.47/api/v1/logs"
            ).insert_error_db())
        
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=results
        )