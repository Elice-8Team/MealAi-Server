from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from enum import Enum


class GenderEnum(str, Enum):
    M = "M"
    F = "F"


class GoalEnum(str, Enum):
    balance = "balance"
    diet = "diet"
    muscle = "muscle"
    lchf = "lchf"


class CreateUserRequest(BaseModel):
    email: EmailStr = Field(..., title="사용자 Email")
    password: str = Field(..., title="사용자 비밀번호")
    gender: GenderEnum = Field(..., title="성별")
    age_group: int = Field(..., gt=0, lt=10, title="연령대")
    nickname: str = Field(..., title="사용자 닉네임")
    goal: GoalEnum = Field(..., title="목표설정")


class EditUserInfoRequest(BaseModel):
    gender: Optional[GenderEnum] = Field(..., title="성별")
    age_group: Optional[int] = Field(..., gt=0, lt=10, title="연령대")
    nickname: Optional[str] = Field(..., title="사용자 닉네임")
    goal: Optional[GoalEnum] = Field(..., title="목표설정")


class CheckPasswordRequest(BaseModel):
    password: str = Field(..., title="비밀번호")


class ChangePasswordRequest(BaseModel):
    current_password: str = Field(..., title="현재 비밀번호")
    change_password: str = Field(..., title="변경할 비밀번호")
