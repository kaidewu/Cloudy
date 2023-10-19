from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "USERS"
    USER_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    USER_CREATED_AT = Column(Integer, nullable=False)
    USER_LOGIN = Column(String(255, collation='utf8mb4_unicode_ci'), unique=True, index=True)
    USER_PASSWORD = Column(String(255, collation='utf8mb4_unicode_ci'), nullable=False)
    USER_MAIL = Column(String(255, collation='utf8mb4_unicode_ci'), index=True)
    USER_PHONE = Column(String(50, collation='utf8mb4_unicode_ci'), unique=True)
    USER_NAME = Column(String(255, collation='utf8mb4_unicode_ci'), nullable=False, index=True)
    USER_SURNAMES = Column(String(255, collation='utf8mb4_unicode_ci'), nullable=False)
    USER_BIRTHDATE = Column(Date, nullable=False)
    USER_ROLE_ID = Column(Integer, ForeignKey('USER_ROLES.USER_ROL_ID'), index=True, nullable=False)
    USER_ACTIVE = Column(Boolean, nullable=False, default=False)
    USER_LAST_LOGIN = Column(String(50, collation='utf8mb4_unicode_ci'), default=None)

class UserRoles(Base):
    __tablename__ = "USER_ROLES"
    USER_ROL_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    USER_ROL_NAME = Column(String(255, collation='utf8mb4_unicode_ci'), unique=True, index=True)
    USER_ROL_DESCRIPTION_ES = Column(Text(collation='utf8mb4_unicode_ci'), default=None)
    USER_ROL_DESCRIPTION_EN = Column(Text(collation='utf8mb4_unicode_ci'), default=None)
    USER_ROL_DELETED = Column(Boolean, default=None)
    USER_ROL_DELETED_DATE = Column(String(50, collation='utf8mb4_unicode_ci'), default=None)

class Wallets(Base):
    __tablename__ = "WALLETS"
    WALLET_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    USER_ID = Column(Integer, ForeignKey('USERS.USER_ID'), index=True, nullable=False)
    WALLET_DELETED = Column(Boolean, default=False)
    WALLET_DELETED_DATE = Column(String(50, collation='utf8mb4_unicode_ci'), default=None)

class Account(Base):
    __tablename__ = "WALLET_ACCOUNTS"
    ACCOUNT_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    WALLET_ID = Column(Integer, ForeignKey('WALLETS.WALLET_ID'), index=True, nullable=False)
    ACCOUNT_NAME = Column(String(255, collation='utf8mb4_unicode_ci'), nullable=False, index=True)
    ACCOUNT_BALANCE = Column(Integer, nullable=False, index=True, default=0)
    ACCOUNT_CURRENCY_TYPES_ID = Column(Integer, ForeignKey('ACCOUNT_CURRENCY_TYPES.ACCOUNT_CURRENCY_TYPES_ID'), nullable=False, index=True)
    ACCOUNT_DELETED = Column(Boolean, default=False)
    ACCOUNT_DELETED_DATE = Column(String(50, collation='utf8mb4_unicode_ci'), default=None)

class AccountCurrencyType(Base):
    __tablename__ = "ACCOUNT_CURRENCY_TYPES"
    ACCOUNT_CURRENCY_TYPES_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ACCOUNT_CURRENCY_TYPES_NAME = Column(String(10, collation='utf8mb4_unicode_ci'), unique=True, nullable=False)
    ACCOUNT_CURRENCY_TYPES_DESCRIPTION_ES = Column(Text(collation='utf8mb4_unicode_ci'), default=None)
    ACCOUNT_CURRENCY_TYPES_DESCRIPTION_EN = Column(Text(collation='utf8mb4_unicode_ci'), default=None)
    ACCOUNT_CURRENCY_TYPES_DEFAULT = Column(Boolean, default=False)
    ACCOUNT_CURRENCY_TYPES_DELETED = Column(Boolean, default=False)
    ACCOUNT_CURRENCY_TYPES_DELETED_DATE = Column(String(50, collation='utf8mb4_unicode_ci'), default=None)

class Categories(Base):
    __tablename__ = "CATEGORIES_TYPES"
    CATEGORY_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    CATEGORY_NAME = Column(String(255, collation='utf8mb4_unicode_ci'), unique=True, nullable=False)
    CATEGORY_ICON_ID = Column(Integer, ForeignKey('CATEGORY_ICONS.CATEGORY_ICON_ID'), unique=True, index=True, nullable=False)
    CATEGORY_DESCRIPTION_ES = Column(Text(collation='utf8mb4_unicode_ci'), default=None)
    CATEGORY_DESCRIPTION_EN = Column(Text(collation='utf8mb4_unicode_ci'), default=None)
    CATEGORY_DESCRIPTION_DELETED = Column(Boolean, default=False)
    CATEGORY_DESCRIPTION_DELETED_DATE = Column(String(50, collation='utf8mb4_unicode_ci'), default=None)

class CategoryIcons(Base):
    __tablename__ = "CATEGORY_ICONS"
    CATEGORY_ICON_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    CATEGORY_ICON_NAME = Column(String(255, collation='utf8mb4_unicode_ci'), unique=True, nullable=False)
    CATEGORY_ICON_URL = Column(Text(collation='utf8mb4_unicode_ci'), default=None)
    CATEGORY_ICON_DESCRIPTION_ES = Column(Text(collation='utf8mb4_unicode_ci'), default=None)
    CATEGORY_ICON_DESCRIPTION_EN = Column(Text(collation='utf8mb4_unicode_ci'), default=None)
    CATEGORY_ICON_DESCRIPTION_DELETED = Column(Boolean, default=False)
    CATEGORY_ICON_DESCRIPTION_DELETED_DATE = Column(String(50, collation='utf8mb4_unicode_ci'), default=None)

class SubCategories(Base):
    __tablename__ = "SUBCATEGORIES_TYPES"
    SUBCATEGORY_TYPE_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    SUBCATEGORY_TYPE_NAME = Column(String(255, collation='utf8mb4_unicode_ci'), unique=True, nullable=False)
    CATEGORY_ICON_ID = Column(Integer, ForeignKey('CATEGORY_ICONS.CATEGORY_ICON_ID'), unique=True, index=True, nullable=False)
    SUBCATEGORY_TYPE_DESCRIPTION_ES = Column(Text(collation='utf8mb4_unicode_ci'), default=None)
    SUBCATEGORY_TYPE_DESCRIPTION_EN = Column(Text(collation='utf8mb4_unicode_ci'), default=None)
    SUBCATEGORY_TYPE_DESCRIPTION_DELETED = Column(Boolean, default=False)
    SUBCATEGORY_TYPE_DESCRIPTION_DELETED_DATE = Column(String(50, collation='utf8mb4_unicode_ci'), default=None)

class RelationCategories(Base):
    __tablename__ = "CATEGORY_SUBCATEGORY_RELATIONS"
    CATEGORY_SUBCATEGORY_RELATION_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    CATEGORY_SUBCATEGORY_RELATION_CATEGORY_ID = Column(Integer, ForeignKey('CATEGORIES_TYPES.CATEGORY_ID'), nullable=False, index=True)
    CATEGORY_SUBCATEGORY_RELATION_SUBCATEGORY_ID = Column(Integer, ForeignKey('SUBCATEGORIES_TYPES.SUBCATEGORY_TYPE_ID'), nullable=False, index=True)
    CATEGORY_SUBCATEGORY_RELATION_DELETED = Column(Boolean, default=False)
    CATEGORY_SUBCATEGORY_RELATION_DELETED_DATE = Column(String(50, collation='utf8mb4_unicode_ci'), default=None)

class Logs(Base):
    __tablename__ = "LOGS"
    LOG_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    LOG_UUID = Column(String(50, collation='utf8mb4_unicode_ci'), nullable=False, index=True)
    LOG_REGISTER_AT = Column(Integer, nullable=False, index=True)
    LOG_LEVEL = Column(Integer, ForeignKey('LOG_LEVEL_TYPES.LOG_LEVEL_TYPE_ID'), nullable=False)
    LOG_BODY = Column(Text(collation='utf8mb4_unicode_ci'), nullable=False)
    #LOG_USER_ID = Column(Integer, ForeignKey('USERS.USER_ID'), index=True, default=None)
    LOG_ENDPOINT = Column(Text(collation='utf8mb4_unicode_ci'), default=None)
    LOG_DELETED = Column(Boolean, default=False)
    LOG_DELETED_DATE = Column(String(50, collation='utf8mb4_unicode_ci'), default=None)

class LogLevels(Base):
    __tablename__ = "LOG_LEVEL_TYPES"
    LOG_LEVEL_TYPE_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    LOG_LEVEL_TYPE_NAME = Column(String(255, collation='utf8mb4_unicode_ci'), nullable=False, index=True)
    LOG_LEVEL_TYPE_DESCRIPTION_ES = Column(Text(collation='utf8mb4_unicode_ci'), default=None)
    LOG_LEVEL_TYPE_DESCRIPTION_EN = Column(Text(collation='utf8mb4_unicode_ci'), default=None)
    LOG_LEVEL_TYPE_DELETED = Column(Boolean, default=False)
    LOG_LEVEL_TYPE_DELETED_DATE = Column(String(50, collation='utf8mb4_unicode_ci'), default=None)