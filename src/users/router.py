from fastapi import APIRouter
from src.schemas import BaseResponse
from src.users.schemas import UserCreate


users_router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@users_router.post(path="", status_code=201)
async def register_user(
    user_in: UserCreate
) -> BaseResponse:
    return BaseResponse(status=True, message=f"User {user_in.email}  successfully registered!")