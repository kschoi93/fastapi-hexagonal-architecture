from fastapi import FastAPI
from app.routers import user


def routes_manager(app: FastAPI):
    app.include_router(user.router)