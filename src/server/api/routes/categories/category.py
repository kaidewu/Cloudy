from fastapi import APIRouter, Depends, status, Query
from fastapi.responses import JSONResponse

from api.routes.error.error_log import Error
from models.Category.models import CreateCategory
from sqlalchemy.orm import Session
from database import models
from database.connection import SessionLocal

import traceback
from datetime import datetime

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
    print(lang)

    try:
        all_categories = (
            db.query(
                models.Categories.CATEGORY_ID,
                models.Categories.CATEGORY_ID_NAME,
                models.Categories.CATEGORY_ID_DESCRIPTION_EN if lang == "en-En" else models.Categories.CATEGORY_ID_DESCRIPTION_ES)
            .filter(
                models.Categories.CATEGORY_ID_DESCRIPTION_DELETED == False)
            .all()
        )

        if (all_categories is None) or (all_categories == []) or (all_categories == "null"):
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content=Error(
                    "Not found any categories",
                    "Not found any categories",
                    status.HTTP_404_NOT_FOUND,
                    "GET http://192.168.1.47/api/v1/category"
                ).insert_error_db()
            )
        
        for category in all_categories:
            categories.append({
                "categoryId": category[0],
                "categoryName": category[1],
                #"categoryIcon": category[2],
                ("categoryDescriptionEN" if lang == "en-En" else "categoryDescriptionES"): category[2]
            })
        
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "status": status.HTTP_200_OK,
                "categories": categories
            }
        )

    except:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=Error(
                traceback.format_exc(),
                traceback.format_exc().splitlines()[-1],
                status.HTTP_500_INTERNAL_SERVER_ERROR,
                "GET http://192.168.1.47/api/v1/category"
            ).insert_error_db()
        )


@category_router.post("/create/category")
async def create_category(
    db: Session = Depends(get_db)
    ):
    try:
        pass
    except:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=Error(
                traceback.format_exc(),
                traceback.format_exc().splitlines()[-1],
                status.HTTP_500_INTERNAL_SERVER_ERROR,
                "POST http://192.168.1.47/api/v1/create/category"
            )
        )