from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from api.routes.error.error_log import Error
from models.Category.models import 
from sqlalchemy.orm import Session
from database import models
from database.connection import SessionLocal

import traceback
from datetime import datetime

category_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@category_router.post("/create/category")
async def create_category(
    db: Session = Depends(get_db)
):
    try:
        pass
    except:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=Error(
                traceback.format_exc(),
                traceback.format_exc().splitlines()[-1],
                status.HTTP_500_INTERNAL_SERVER_ERROR,
                "POST http://192.168.1.47/api/v1/create/category"
            )
        )