from fastapi import FastAPI


def create_app():
    app = FastAPI()
    from app.router_manager import routes_manager
    routes_manager(app)
    return app

app = create_app()