from fastapi import APIRouter, Depends, status, HTTPException

from sqlalchemy.orm import Session
from database.connection import SessionLocal
from database import models
from api.routes.error.error_log import Error

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
    db: Session = Depends(get_db)):

    results = {}

    try:
        wallets = []

        user = db.query(
                models.User.USER_ID,
                models.User.USER_NAME,
                models.User.USER_SURNAMES,
                models.User.USER_MAIL
                ).filter(models.User.USER_ID == user_id,
                         models.User.USER_ACTIVE == True).first()

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
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"The user {user_id} wallet not exists"
            )
        
        if (user is None) or (user == []) or (user == "null"):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"The user {user_id} not exists"
            )

        for wallet in user_wallets:
            wallets.append({
                "walletId": wallet[0],
                "accountName": wallet[1],
                "accountBalance": wallet[2],
                "accountCurrency": wallet[3]
            })

        results.update({
            "status": status.HTTP_200_OK,
            "user": {
                "userId": user[0],
                "userName": user[1],
                "userSurname": user[2],
                "userMail": user[3],
            },
            "userWallets": wallets
        })

        return results

    except HTTPException as http_exception:
        if http_exception.detail == f"The user {user_id} wallet not exists":
            results.update(Error(
                    f"The user {user_id} wallet not exists",
                    f"The user {user_id} wallet not exists",
                    status.HTTP_404_NOT_FOUND,
                    f"http://192.168.1.47/api/v1/{user_id}/wallet"
                ).insert_error_db())
        if http_exception.detail == f"The user {user_id} not exists":
            results.update(Error(
                    f"The user {user_id} not exists",
                    f"The user {user_id} not exists",
                    status.HTTP_404_NOT_FOUND,
                    f"http://192.168.1.47/api/v1/{user_id}/wallet"
                ).insert_error_db())

        raise HTTPException(
            status_code=http_exception.status_code,
            detail=results
        )

    except Exception as exception:
        results.update(Error(
            traceback.format_exc(),
            str(exception),
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            f"http://192.168.1.47/api/v1/{user_id}/wallet"
        ).insert_error_db())

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=results
        )