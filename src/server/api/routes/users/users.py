from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from database.connection import SessionLocal
from database import models
from api.routes.error.error_log import Error
from models import CreateUser
from api.routes.users.utils import hash_password

import traceback
import time
from datetime import datetime

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
    users = []

    try:
        all_users = (
            db.query(
                models.User.USER_ID,
                models.User.USER_NAME,
                models.User.USER_SURNAMES,
                models.User.USER_CREATED_AT,
                models.User.USER_LOGIN,
                models.User.USER_MAIL,
                models.User.USER_PHONE,
                models.User.USER_BIRTHDATE,
                models.User.USER_LAST_LOGIN,
                models.User.USER_ACTIVE)
            .all()
        )
        
        if (all_users is None) or (all_users == []) or (all_users == "null"):
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content=Error(
                    "Not Exists Users",
                    "Not Exists Users",
                    status.HTTP_400_BAD_REQUEST,
                    "GET http://192.168.1.47/api/v1/users"
                ).insert_error_db()
            )
        
        for user in all_users:
            users.append({
                "userId": user[0],
                "userName": user[1],
                "userSurname": user[2],
                "userCreateAt": datetime.fromtimestamp(user[3]).strftime("%Y-%m-%d %H:%M:%S.%M"),
                "userLogin": user[4],
                "userMail": user[5],
                "userPhone": user[6],
                "userBirthdate": user[7],
                "userLastLogin": user[8],
                "userActive": user[9]
            })

        return {
            "status": status.HTTP_200_OK,
            "data": users
        }

    except:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=Error(
                traceback.format_exc(),
                traceback.format_exc().splitlines()[-1],
                status.HTTP_500_INTERNAL_SERVER_ERROR,
                f"GET http://192.168.1.47/api/v1/users"
            ).insert_error_db()
        )
    
@users_router.post("/create/user", summary="Create Users")
async def create_user(
    user: CreateUser,
    db: Session = Depends(get_db)
    ):

    try:
        if user.user_birthdate is not None:
            try:
                datetime.strptime(user.user_birthdate, "%Y-%m-%d")
            except ValueError:
                return JSONResponse(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
                content=Error(
                    "Invalid date format. Date should be in the format 'YYYY-MM-DD'",
                    "Invalid date format. Date should be in the format 'YYYY-MM-DD'",
                    status.HTTP_422_UNPROCESSABLE_ENTITY,
                    "POST http://192.168.1.47/api/v1/create/user"
                ).insert_error_db()
            )

        if len(''.join(filter(str.isdigit, user.user_phone))) != 9:
            return JSONResponse(
                    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
                    content=Error(
                        "Invalid phone number format. Phone number should be 9 digits",
                        "Invalid phone number format. Phone number should be 9 digits",
                        status.HTTP_422_UNPROCESSABLE_ENTITY,
                        "POST http://192.168.1.47/api/v1/create/user"
                    ).insert_error_db()
                )

        if db.query(models.User).filter(models.User.USER_LOGIN == user.user_login).first():
            return JSONResponse(
                status_code=status.HTTP_409_CONFLICT,
                content=Error(
                    f"The username {user.user_login} already exists",
                    f"The username {user.user_login} already exists",
                    status.HTTP_409_CONFLICT,
                    "POST http://192.168.1.47/api/v1/create/user"
                ).insert_error_db()
            )
        
        if db.query(models.User).filter(models.User.USER_MAIL == user.user_mail).first():
            return JSONResponse(
                status_code=status.HTTP_409_CONFLICT,
                content=Error(
                    f"The mail {user.user_mail} already exists",
                    f"The mail {user.user_mail} already exists",
                    status.HTTP_409_CONFLICT,
                    "POST http://192.168.1.47/api/v1/create/user"
                ).insert_error_db()
            )

        if db.query(models.User).filter(models.User.USER_PHONE == user.user_phone).first():
            return JSONResponse(
                status_code=status.HTTP_409_CONFLICT,
                content=Error(
                    f"The phone number {user.user_phone} already exists",
                    f"The phone number {user.user_phone} already exists",
                    status.HTTP_409_CONFLICT,
                    "POST http://192.168.1.47/api/v1/create/user"
                ).insert_error_db()
            )

        insert_user = models.User(
            USER_CREATED_AT = int(time.time()),
            USER_LOGIN = user.user_login,
            USER_PASSWORD = hash_password(user.user_password),
            USER_MAIL = user.user_mail,
            USER_PHONE = user.user_phone,
            USER_NAME = user.user_name,
            USER_SURNAMES = user.user_surnames,
            USER_BIRTHDATE = user.user_birthdate,
            USER_ACTIVE = False,
            USER_LAST_LOGIN = None
        )
        db.add(insert_user)
        db.commit()
        db.refresh(insert_user)

        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "status": status.HTTP_201_CREATED,
                "message": "User Created"
            }
        )
    
    except:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=Error(
                traceback.format_exc(),
                traceback.format_exc().splitlines()[-1],
                status.HTTP_500_INTERNAL_SERVER_ERROR,
                f"POST http://192.168.1.47/api/v1/create/user"
            ).insert_error_db()
        )