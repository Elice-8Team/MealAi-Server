import datetime

from pydantic import BaseModel, Field
from typing import List, Union
from app.dto.feed.FeedRequest import Food, MealTimeEnum, GoalEnum
from app.dto.report.ReportResponse import ReportGoal


class FeedData(BaseModel):
    feed_id: int = Field(..., title="피드 ID")
    user_id: int = Field(..., title="작성자 ID")
    image_url: Union[str, None] = Field(..., title="전체 이미지 URL")
    user_name: str = Field(..., title="작성자 이름")
    meal_time: MealTimeEnum = Field(
        ..., title="식사 종류", description="balance,lunch,dinner,snack"
    )
    date: datetime.date = Field(..., title="식사 날짜")
    user_daily_nutrient: Union[ReportGoal, None] = Field(..., title="유저 하루 목표치")
    likes: int = Field(..., title="좋아요 수")
    kcal: float = Field(..., title="전체 열량")
    carbohydrate: float = Field(..., title="전체 탄수화물")
    protein: float = Field(..., title="전체 단백질")
    fat: float = Field(..., title="전체 지방")
    foods: List[Food] = Field(..., title="먹은 음식들")
    created_at: datetime.datetime = Field(..., title="생성 일자")
    updated_at: datetime.datetime = Field(..., title="수정 일자")
    open: bool = Field(..., title="공개 여부", description="True or False")
    goal: GoalEnum = Field(..., title="피드 카테고리")
    my_like: bool = Field(..., title="좋아요 여부", description="True or False")
    is_mine: bool = Field(..., title="나의 글인지 여부", description="True or False")

    class Config:
        orm_mode = True


class GetFeedsResponse(BaseModel):
    prev_page: bool = Field(..., title="이전페이지 여부", description="True or False")
    next_page: bool = Field(..., title="다음 페이지 여부", description="True or False")
    feeds: List[FeedData] = Field(..., title="FeedData 배열", description="피드 배열")

    class Config:
        orm_mode = True


class FoodInfo(BaseModel):
    food_id: int = Field(..., title="음식 id")
    name: str = Field(..., title="음식 이름")
    weight: float = Field(..., title="음식의 양")
    kcal: float = Field(...,title="kcal")
    carbohydrate: float = Field(..., title="탄수화물")
    protein: float = Field(..., title="단백질")
    fat: float = Field(..., title="지방")

class NutrientInfo(BaseModel):
    kcal: float = Field(..., title="kcal")
    carbohydrate: float = Field(..., title="탄수화물")
    protein: float = Field(..., title="단백질")
    fat: float = Field(..., title="지방")