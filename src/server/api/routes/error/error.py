from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from sqlalchemy import and_
from sqlalchemy.orm import Session
from database.connection import SessionLocal
from database import models
from api.routes.error.error_log import Error
from constants import ENV_VARS, DATETIME_FORMAT

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
    all_logs = []
    filters = []
    response = 0

    try:
        if startDate is not None and startDate != "":
            filters.append(models.Logs.LOG_REGISTER_AT >= startDate)

        if endDate is not None and endDate != "":
            filters.append(models.Logs.LOG_REGISTER_AT <= endDate)

        if errorId is not None and errorId != "":
            filters.append(models.Logs.LOG_UUID == errorId)

        get_logs = (
            db.query(
                models.Logs.LOG_UUID,
                models.Logs.LOG_REGISTER_AT,
                models.Logs.LOG_BODY,
                models.Logs.LOG_ENDPOINT,
                models.Logs.LOG_LEVEL)
                .filter(models.Logs.LOG_DELETED == False,
                        (and_(*filters)))
                .all()
            )

        if (get_logs is None) or (get_logs == []) or (get_logs == "null"):
            response = status.HTTP_404_NOT_FOUND
            raise ValueError(f"{errorId} not exists" if (errorId is not None) and (errorId != "") else "Not register Logs yet")
        
        for log in get_logs:
            all_logs.append({
                "logId": log[0],
                "logRegisterAt": datetime.fromtimestamp(log[1]).strftime(DATETIME_FORMAT),
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
        if response == 0:
            response = status.HTTP_500_INTERNAL_SERVER_ERROR
        return JSONResponse(
                status_code=response, 
                content=Error(
                    traceback.format_exc(),
                    traceback.format_exc().splitlines()[-1],
                    response,
                    f"GET {ENV_VARS['API_ENDPOINT']}logs"
                ).insert_error_db()
            )