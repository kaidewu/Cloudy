from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from api.routes.users.users import users_router
from api.routes.mywallet.mywallet import wallet_router
import uvicorn

from database.connection import SessionLocal, engine
from database.models import Base

from dotenv import dotenv_values
import os

env_vars = dotenv_values(f"{os.path.dirname(__file__)}/.env")

# Configure CORS
origins = [
        "http://192.168.1.47:3000",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://[::1]:3000"
    ]

app = FastAPI()

app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE"],
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
        tags=["users"],
    )

# Check if tables exist, create them if not
Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80, reload=True)