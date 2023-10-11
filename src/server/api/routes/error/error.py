from fastapi import APIRouter, Depends, status

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
        if (error_uuid is None) or (error_uuid == ""):
            get_errors = db.query(models.Logs).filter(models.Logs.LOG_DELETED == False).all()
        else:
            get_errors = db.query(models.Logs).filter(models.Logs.LOG_UUID == error_uuid, models.Logs.LOG_DELETED == False).first()

        if (get_errors is None) or (get_errors == []):
            results.update(Error(
                f"{error_uuid} not exists" if (error_uuid is not None) or (error_uuid != "") else "Not register Logs yet",
                f"{error_uuid} not exists" if (error_uuid is not None) or (error_uuid != "") else "Not register Logs yet",
                status.HTTP_400_BAD_REQUEST,
                "http://192.168.1.47/api/v1/logs"
            ).insert_error_db())

            return results
        
        results = {
            "status": status.HTTP_200_OK,
            "logs": get_errors
        }

        return results
        
    except:
        results.update(Error(
                traceback.format_exc(),
                traceback.format_exc().splitlines()[-1],
                status.HTTP_500_INTERNAL_SERVER_ERROR,
                "http://192.168.1.47/api/v1/logs"
            ).insert_error_db())