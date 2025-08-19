from pydantic import BaseModel, EmailStr


class MessageSchema(BaseModel):
    message: str


class UserSchema(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserPublicSchema(BaseModel):
    name: str
    email: EmailStr
