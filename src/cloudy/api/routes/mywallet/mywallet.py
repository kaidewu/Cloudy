from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session
from database.connection import SessionLocal
from database import models
from api.routes.error.error_log import Error

import sys
import traceback

wallet_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@wallet_router.get("/user/{user_id}/wallet", response_description="List user wallet information")
async def get_user_wallet(
    user_id: int,
    db: Session = Depends(get_db)
    ):
    results = {}

    try:
        wallets = []

        user_wallets = (
            db.query(
                models.Wallet.USER_ID,
                models.User.USER_NAME,
                models.User.USER_SURNAMES,
                models.User.USER_MAIL,
                models.Account.ACCOUNT_NAME,
                models.Account.ACCOUNT_BALANCE,
                models.AccountCurrencyType.ACCOUNT_CURRENCY_TYPES_NAME
            )
            .join(models.User)
            .join(models.Account)
            .join(models.AccountCurrencyType)
            .filter(models.Wallet.USER_ID == user_id,
                    models.Wallet.WALLET_DELETED == False,
                    models.User.USER_ACTIVE == 1,
                    models.AccountCurrencyType.ACCOUNT_CURRENCY_TYPES_DELETED == False,
                    models.Account.ACCOUNT_DELETED == False)
            .all()
        )

        if (user_wallets is None) or (user_wallets == []):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={
                    "statusCode": status.HTTP_400_BAD_REQUEST,
                    "message": f"The user {user_id} wallet not exists"
                }
            )
        
        for wallet in user_wallets:
            wallets.append({
                "userId": wallet[0],
                "userName": wallet[1],
                "userSurname": wallet[2],
                "userMail": wallet[3],
                "accountName": wallet[4],
                "accountBalance": wallet[5],
                "accountCurrency": wallet[6]
            })

        results.update({
            "status": status.HTTP_200_OK,
            "userWallets": wallets
        })

        return results
    except:
        results.update(Error(
            traceback.format_exc(),
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            f"http://192.168.1.47/api/v1/{user_id}/wallet"
        ).insert_error_db())
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=results
        )