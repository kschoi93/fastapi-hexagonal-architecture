from fastapi import FastAPI


def create_app():
    app = FastAPI()
    # from main.router_manager import routes_manager
    # routes_manager(app)
    # from main.adapter.inbound.web import bank_account_controller
    # app.include_router(bank_account_controller.router)
    from src.main.msa.interface.adapter.user.inbound import user_controller
    app.include_router(user_controller.router)
    return app

app = create_app()