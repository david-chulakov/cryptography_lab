from fastapi import FastAPI
from src.users.router import users_router

app = FastAPI(
    debug=True,
    title="Сервис для криптографии",
    version="0.1.0"
)

app.include_router(router=users_router)