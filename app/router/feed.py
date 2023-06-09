from fastapi import APIRouter, Form
from app.dto.feed.FeedRequest import *
from app.dto.feed.FeedResponse import *
from app.service.like import *
from app.utils.depends import *

router = APIRouter(
    prefix="/api/feeds",
)


@router.post(
    "",
    description="피드 작성",
    response_model=int,
    tags=["feed"],
)
async def post_feed(
    meal_time: MealTimeEnum = Form(),
    date: str = Form(),
    file: UploadFile = File(),
    user_id: int = Depends(current_user_id_for_feed),
):
    req = {"meal_time": meal_time, "date": date}
    return await FeedService().service_post_feed(req, user_id, file)


@router.get(
    "",
    description="전체 피드 조회",
    response_model=GetFeedsResponse,
    tags=["feed"],
)
async def get_feeds(
    goal: GoalEnum = "all",
    filter: FilterEnum = "newest",
    page: int = 1,
    per_page: int = 10,
    user_id: int = Depends(current_user_id_for_feed),
):
    return await FeedService().service_get_feeds(goal, filter, page, per_page, user_id)


@router.get(
    "/likes",
    description="내가 좋아요한 피드",
    response_model=GetFeedsResponse,
    tags=["feed"],
)
async def get_my_likes(
    page: int = 1, per_page: int = 10, user_id: int = Depends(current_user_id)
):
    return await LikeService().service_get_my_likes_feeds(page, per_page, user_id)


@router.patch(
    "/likes/{feed_id}",
    description="좋아요 토글",
    response_model=str,
    tags=["feed"],
)
def patch_likes_by_id(feed_id: int, user_id: int = Depends(current_user_id)):
    return LikeService().service_patch_likes_by_id(feed_id, user_id)


@router.get(
    "/{feed_id}",
    description="상세 피드 조회",
    response_model=FeedData,
    tags=["feed"],
)
async def get_feed_by_id(
    feed_id: int, user_id: int = Depends(current_user_id_for_feed)
):
    return await FeedService().service_get_feed_by_id(feed_id, user_id)


@router.patch(
    "/{feed_id}",
    description="피드 수정",
    response_model=FeedData,
    tags=["feed"],
)
async def patch_feed_by_id(
    feed_id: int, req: PatchFeedData, user_id: int = Depends(current_user_id_for_feed)
) -> FeedData:
    return await FeedService().service_patch_feed(feed_id, req, user_id)


@router.delete(
    "/{feed_id}",
    description="피드 삭제",
    # response_model=str,
    tags=["feed"],
)
def delete_feed_by_id(feed_id: int, user_id: int = Depends(current_user_id)):
    return FeedService().service_delete_feed(feed_id, user_id)


@router.get(
    "/food/{food_name}",
    description="음식 찾기",
    response_model=List[FoodInfo],
    tags=["feed"],
)
def search_food_by_name(
    food_name: str,
):
    return FeedService().service_search_food_by_name(food_name)


@router.post(
    "/food",
    description="음식 영양소 정보 얻기",
    response_model=NutrientInfo,
    tags=["feed"],
)
def search_food_by_name(foods: List[FoodRequest]):
    data, nutrient = FeedService().service_get_food_info_by_data(foods)
    return nutrient
