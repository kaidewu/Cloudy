from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from database.connection import SessionLocal
from database import models

users_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@users_router.get("/users", response_description="List all users")
def get_users(
    db: Session = Depends(get_db)
    ):
    all_users = db.query(models.User).filter(models.User.USER_ACTIVE == True).all()
    return all_users