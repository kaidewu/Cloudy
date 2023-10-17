from fastapi import FastAPI, status, Response
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from database.connection import engine
from database.models import Base

from api.routes.users.users import users_router
from api.routes.mywallet.mywallet import wallet_router
from api.routes.error.error import error_router
from api.routes.categories.category import category_router

from dotenv import dotenv_values
import os

env_vars = dotenv_values(f"{os.path.dirname(__file__)}/.env")

# Configure CORS
origins = ["*"]

app = FastAPI()

app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT"],
        allow_headers=["Authorization", "Content-Type"],
    )

app.include_router(
        users_router,
        prefix="/api/v1",
        tags=["users"],
    )

app.include_router(
        wallet_router,
        prefix="/api/v1",
        tags=["wallet"],
    )

app.include_router(
        error_router,
        prefix="/api/v1",
        tags=["logs"],
    )

app.include_router(
        category_router,
        prefix="/api/v1",
        tags=["category"],
    )

@app.get("/favicon.ico")
def favicon(response: Response):
    response.status_code=status.HTTP_200_OK
    return FileResponse(f"{os.path.dirname(__file__)}/public/favicon.ico")

# Check if tables exist, create them if not
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80, reload=True)