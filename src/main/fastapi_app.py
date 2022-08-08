from fastapi import FastAPI


def create_app():
    app = FastAPI()
    # routes
    from src.main.routes import routes_manager
    routes_manager(app)

    return app


app = create_app()