from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session
from database.connection import SessionLocal
from database import models
from api.routes.error.error_log import Error

import traceback

users_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@users_router.get("/users", response_description="List all users")
async def get_users(
    db: Session = Depends(get_db)
    ):
    results = {}

    try:
        all_users = db.query(models.User).filter(models.User.USER_ACTIVE == True).all()
        if (all_users is None) or (all_users == []):
            results = {
                    "statusCode": status.HTTP_400_BAD_REQUEST,
                    "message": "Users are not registered"
                }
            results.update(Error(
                    "Not Exists Users",
                    "Not Exists Users",
                    status.HTTP_400_BAD_REQUEST,
                    f"http://192.168.1.47/api/v1/users"
                ).insert_error_db())
            return results
        
        results.update({
            "status": status.HTTP_200_OK,
            "data": all_users
        })

        return results 

    except:
        results.update(Error(
            traceback.format_exc(),
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            f"http://192.168.1.47/api/v1/users"
        ).insert_error_db())

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": "Internal Error"
            }
        )