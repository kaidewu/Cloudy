from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from database.connection import SessionLocal
from database import models

wallet_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@wallet_router.get("/user/{user_id}/wallet", response_description="List user wallet information")
def get_user_wallet(
    user_id: int,
    db: Session = Depends(get_db)
    ):
    user_wallet = (
        db.query(
            models.Wallet.USER_ID,
            models.User.USER_NAME,
            models.User.USER_SURNAMES,
            models.User.USER_MAIL,
            models.Account.ACCOUNT_NAME,
            models.Account.ACCOUNT_CURRENCY_TYPES_ID,
            models.Account.ACCOUNT_BALANCE,
            models.AccountCurrencyType.ACCOUNT_CURRENCY_TYPES_NAME,
            models.AccountCurrencyType.ACCOUNT_CURRENCY_TYPES_DESCRIPTION_EN
        )
        .join(models.User)
        .join(models.Account)
        .join(models.AccountCurrencyType)
        .filter(models.Wallet.USER_ID == user_id, 
                models.User.USER_ACTIVE == 1,
                models.AccountCurrencyType.ACCOUNT_CURRENCY_TYPES_DELETED == 0,
                models.Account.ACCOUNT_DELETED == 0)
        .all()
    )

    return {"data": str(user_wallet)}