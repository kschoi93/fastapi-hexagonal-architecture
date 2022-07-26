from pydantic import BaseModel, EmailStr


class UserEntity(BaseModel):
    username: str
    # email: EmailStr
    # password: str