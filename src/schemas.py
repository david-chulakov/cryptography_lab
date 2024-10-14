from pydantic import BaseModel


class BaseResponse(BaseModel):
    status: bool
    message: str
    detail: str | None = None