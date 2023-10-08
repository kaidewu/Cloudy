from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "USERS"
    USER_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    USER_CREATED_AT= Column(String(50), nullable=False)
    USER_LOGIN= Column(String(255, collation='utf8mb4_unicode_ci'), unique=True, index=True)
    USER_PASSWORD= Column(String(255, collation='utf8mb4_unicode_ci'), nullable=False)
    USER_MAIL= Column(String(255, collation='utf8mb4_unicode_ci'), index=True)
    USER_PHONE= Column(String(50), unique=True)
    USER_NAME= Column(String(255, collation='utf8mb4_unicode_ci'), nullable=False, index=True)
    USER_SURNAMES= Column(String(255, collation='utf8mb4_unicode_ci'), nullable=False)
    USER_BIRTHDATE= Column(Date, nullable=False)
    USER_ACTIVE= Column(Boolean, nullable=False, default=False)
    USER_LAST_LOGIN= Column(String(50), default=None)

class Wallet(Base):
    __tablename__ = "WALLETS"
    WALLET_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    USER_ID = Column(Integer, ForeignKey('USERS.USER_ID'), index=True, nullable=False, unique=True)
    WALLET_DELETED = Column(Boolean, default=False)
    WALLET_DELETED_DATE = Column(String(50), default=None)

class Account(Base):
    __tablename__ = "WALLET_ACCOUNTS"
    ACCOUNT_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    WALLET_ID = Column(Integer, ForeignKey('WALLETS.WALLET_ID'), index=True, nullable=False, unique=True)
    ACCOUNT_NAME = Column(String(255, collation='utf8mb4_unicode_ci'), nullable=False, unique=True, index=True)
    ACCOUNT_BALANCE = Column(Integer, nullable=False, unique=True, index=True, default=0)
    ACCOUNT_CURRENCY_TYPES_ID = Column(Integer, ForeignKey('ACCOUNT_CURRENCY_TYPES.ACCOUNT_CURRENCY_TYPES_ID'), nullable=False, unique=True, index=True)
    ACCOUNT_DELETED = Column(Boolean, default=False)
    ACCOUNT_DELETED_DATE = Column(String(50), default=None)

class AccountCurrencyType(Base):
    __tablename__ = "ACCOUNT_CURRENCY_TYPES"
    ACCOUNT_CURRENCY_TYPES_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ACCOUNT_CURRENCY_TYPES_NAME = Column(String(10, collation='utf8mb4_unicode_ci'), unique=True, nullable=False)
    ACCOUNT_CURRENCY_TYPES_DESCRIPTION_ES = Column(Text(collation='utf8mb4_unicode_ci'), default=None)
    ACCOUNT_CURRENCY_TYPES_DESCRIPTION_EN = Column(Text(collation='utf8mb4_unicode_ci'), default=None)
    ACCOUNT_CURRENCY_TYPES_DEFAULT = Column(Boolean, default=False)
    ACCOUNT_CURRENCY_TYPES_DELETED = Column(Boolean, default=False)
    ACCOUNT_CURRENCY_TYPES_DELETED_DATE = Column(String(50), default=None)