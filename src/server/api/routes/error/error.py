from fastapi import APIRouter, Depends, status

from sqlalchemy import or_
from sqlalchemy.orm import Session
from database.connection import SessionLocal
from database import models
from api.routes.error.error_log import Error

import traceback

error_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@error_router.get("/logs", summary="Get logs of the application. Warnings or Errors")
async def get_logs(
    error_uuid: str = None,
    db: Session = Depends(get_db)
):
    results = {}

    try:
        all_logs = []

        get_logs = (
            db.query(
                models.Logs.LOG_UUID,
                models.Logs.LOG_REGISTER_AT,
                models.Logs.LOG_BODY,
                models.Logs.LOG_ENDPOINT,
                models.LogLevels.LOG_LEVEL_TYPE_NAME)
                .join(models.LogLevels, models.Logs.LOG_LEVEL == models.LogLevels.LOG_LEVEL_TYPE_ID)
                .filter(
                    models.Logs.LOG_DELETED == False,
                    models.LogLevels.LOG_LEVEL_TYPE_DELETED == False,
                    or_(
                        models.Logs.LOG_UUID == error_uuid,
                        error_uuid is not None,
                        error_uuid != ""
                    )
            ).all()
        )

        if (get_logs is None) or (get_logs == []):
            results.update(Error(
                f"{error_uuid} not exists" if (error_uuid is not None) or (error_uuid != "") else "Not register Logs yet",
                f"{error_uuid} not exists" if (error_uuid is not None) or (error_uuid != "") else "Not register Logs yet",
                status.HTTP_400_BAD_REQUEST,
                "http://192.168.1.47/api/v1/logs"
            ).insert_error_db())

            return results
        
        for log in get_logs:
            all_logs.append({
                "logId": log[0],
                "logRegisterAt": log[1],
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