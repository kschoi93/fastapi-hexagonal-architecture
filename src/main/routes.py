from fastapi import FastAPI

from src.main.msa.interface.adapter.user.inbound import user_controller, upload_controller


def routes_manager(app: FastAPI):
    app.include_router(user_controller.router, prefix='/user')
    app.include_router(upload_controller.router, prefix='/upload')