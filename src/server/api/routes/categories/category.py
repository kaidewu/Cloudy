from fastapi import APIRouter, Depends, status, Query
from fastapi.responses import JSONResponse

from api.routes.error.error_log import Error
from models.Category.models import CreateCategory
from sqlalchemy.orm import Session
from database import models
from database.connection import SessionLocal
from constants import ENV_VARS

import traceback


category_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@category_router.get("/category", summary="Get all categories")
async def caterogies(
    lang: str = Query("en-EN", title="Language", description="Language code (es-ES or en-EN)", regex="^(es-ES|en-EN)$"),
    db: Session = Depends(get_db)
    ):
    categories = []
    response = 0

    try:
        all_categories = (
            db.query(
                models.Categories.CATEGORY_ID,
                models.Categories.CATEGORY_NAME,
                models.Categories.CATEGORY_ICON_ID,
                models.CategoryIcons.CATEGORY_ICON_URL,
                models.Categories.CATEGORY_DESCRIPTION_EN if (lang == "en-EN") or (lang == "") else models.Categories.CATEGORY_DESCRIPTION_ES)
            .select_from(models.Categories)
            .join(models.CategoryIcons, models.Categories.CATEGORY_ICON_ID == models.CategoryIcons.CATEGORY_ICON_ID)
            .filter(
                models.Categories.CATEGORY_DESCRIPTION_DELETED == False,
                models.CategoryIcons.CATEGORY_ICON_DESCRIPTION_DELETED == False)
            .all()
        )

        if (all_categories is None) or (all_categories == []) or (all_categories == "null"):
            response = status.HTTP_404_NOT_FOUND
            raise ValueError("Not found any categories")
        
        for category in all_categories:
            categories.append({
                "categoryId": category[0],
                "categoryName": category[1],
                "categoryIconId": category[2],
                "categoryIconURL": category[3],
                ("categoryDescriptionEN" if (lang == "en-EN") or (lang == "") else "categoryDescriptionES"): category[4]
            })
        
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "status": status.HTTP_200_OK,
                "categories": categories
            }
        )

    except:
        if response == 0:
            response = status.HTTP_500_INTERNAL_SERVER_ERROR
        return JSONResponse(
            status_code=response,
            content=Error(
                traceback.format_exc(),
                traceback.format_exc().splitlines()[-1],
                response,
                f"GET {ENV_VARS['API_ENDPOINT']}category"
            ).insert_error_db()
        )

@category_router.get("/category/icons", summary="Get icons of categories if it is not in uses")
async def category_icons(
    db: Session = Depends(get_db)
    ):
    category_icons = []
    response = 0

    try:
        all_category_icons = (
            db.query(
                models.CategoryIcons.CATEGORY_ICON_ID,
                models.CategoryIcons.CATEGORY_ICON_NAME,
                models.CategoryIcons.CATEGORY_ICON_URL
            )
            .outerjoin(models.Categories, models.Categories.CATEGORY_ICON_ID == models.CategoryIcons.CATEGORY_ICON_ID)
            .outerjoin(models.SubCategories, models.SubCategories.CATEGORY_ICON_ID == models.CategoryIcons.CATEGORY_ICON_ID)
            .filter(
                (models.Categories.CATEGORY_ICON_ID == None) & (models.SubCategories.CATEGORY_ICON_ID == None),
                models.CategoryIcons.CATEGORY_ICON_DESCRIPTION_DELETED == False
            )
            .all()
        )

        if (all_category_icons is None) or (all_category_icons == []) or (all_category_icons == "null"):
            response = status.HTTP_404_NOT_FOUND
            raise ValueError("Not found any category Icons")
        
        for icon in all_category_icons:
            category_icons.append({
                "categoryIconId": icon[0],
                "categoryIconName": icon[1],
                "categoryIconURL": icon[2]
            })

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "status": status.HTTP_200_OK,
                "categoryIcons": category_icons
            }
        )

    except:
        if response == 0:
            response = status.HTTP_500_INTERNAL_SERVER_ERROR
        return JSONResponse(
            status_code=response,
            content=Error(
                traceback.format_exc(),
                traceback.format_exc().splitlines()[-1],
                response,
                f"GET {ENV_VARS['API_ENDPOINT']}category/icons"
            )
        )

@category_router.post("/create/category")
async def create_category(
    category: CreateCategory,
    db: Session = Depends(get_db)
    ):

    response = 0
    try:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "status": status.HTTP_200_OK,
                "message": f"The category '{category.categoryName}' has been created succesfully"
            }
        )
    except:
        if response == 0:
            response = status.HTTP_500_INTERNAL_SERVER_ERROR
        return JSONResponse(
            status_code=response,
            content=Error(
                traceback.format_exc(),
                traceback.format_exc().splitlines()[-1],
                response,
                f"POST {ENV_VARS['API_ENDPOINT']}create/category"
            )
        )