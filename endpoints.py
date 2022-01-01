from fastapi import FastAPI


def define_end_points(app: FastAPI):
    @app.get("/")
    async def root():
        return {'message': "Hello World"}

    return app

