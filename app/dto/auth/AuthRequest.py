from pydantic import BaseModel, Field, EmailStr


class LoginRequest(BaseModel):
    email: EmailStr = Field(..., title="사용자 Email")
    password: str = Field(..., title="사용자 비밀번호")


class EmailRequest(BaseModel):
    email: EmailStr = Field(..., title="사용자 Email")


class LogoutRequest(BaseModel):
    user_id: int = Field(..., title="user_id")
    access_token: str = Field(..., title="refresh Token")
