from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from database.connection import SessionLocal
from database import models
from api.routes.error.error_log import Error
from constants import ENV_VARS

import traceback

wallet_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@wallet_router.get("/user/{user_id}/wallet", summary="List user wallet information")
async def get_user_wallet(
    user_id: str = None,
    db: Session = Depends(get_db)
    ):
    wallets = []
    response = 0

    try:
        user = (
            db.query(
                models.User.USER_ID,
                models.User.USER_NAME,
                models.User.USER_SURNAMES,
                models.User.USER_MAIL)
            .filter(models.User.USER_ID == user_id,
                    models.User.USER_ACTIVE == True)
            .first()
            )

        user_wallets = (
            db.query(
                models.Wallets.WALLET_ID,
                models.Account.ACCOUNT_NAME,
                models.Account.ACCOUNT_BALANCE,
                models.AccountCurrencyType.ACCOUNT_CURRENCY_TYPES_NAME)
            .join(models.Account, models.Wallets.WALLET_ID == models.Account.WALLET_ID)
            .join(models.AccountCurrencyType, models.Account.ACCOUNT_CURRENCY_TYPES_ID == models.AccountCurrencyType.ACCOUNT_CURRENCY_TYPES_ID)
            .filter(models.Wallets.USER_ID == user_id,
                    models.Wallets.WALLET_DELETED == False,
                    models.AccountCurrencyType.ACCOUNT_CURRENCY_TYPES_DELETED == False,
                    models.Account.ACCOUNT_DELETED == False)
            .all()
            )

        if (user_wallets is None) or (user_wallets == []) or (user_wallets == "null"):
            response = status.HTTP_404_NOT_FOUND
            raise ValueError(f"The user {user_id} wallet not exists")
        
        if (user is None) or (user == []) or (user == "null"):
            response = status.HTTP_404_NOT_FOUND
            raise ValueError(f"The user {user_id} not exists")

        for wallet in user_wallets:
            wallets.append({
                "walletId": wallet[0],
                "accountName": wallet[1],
                "accountBalance": wallet[2],
                "accountCurrency": wallet[3]
            })

        return {
            "status": status.HTTP_200_OK,
            "user": {
                "userId": user[0],
                "userName": user[1],
                "userSurname": user[2],
                "userMail": user[3],
            },
            "userWallets": wallets
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
                    f"GET {ENV_VARS['API_ENDPOINT']}{user_id}/wallet"
                ).insert_error_db()
            )