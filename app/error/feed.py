from app.error.base import CustomException


class NoFeedIdException(CustomException):
    status = 404
    error_code = 3001
    error_name = "NoFeedId"
    message = "해당 아이디의 피드가 없습니다."


class DeleteFeedException(CustomException):
    status = 404
    error_code = 3002
    error_name = "DeleteFeedError"
    message = "해당 피드를 삭제할 수 없습니다."


class UpdateFeedException(CustomException):
    status = 404
    error_code = 3003
    error_name = "UpdateFeedError"
    message = "해당 피드를 수정할 수 없습니다."


class UnauthorizedFeedException(CustomException):
    status = 403
    error_code = 3004
    error_name = "UnauthorizedFeedError"
    message = "해당 피드의 권한이 없습니다."


class PostException(CustomException):
    status = 500
    error_code = 3005
    error_name = "FeedPostServerError"
    message = "서버 내부 에러 입니다."


class FailedPredictionException(CustomException):
    status = 400
    error_code = 3014
    error_name = "FAILED_PREDICTION"
    message = "이미지 분석에 실패했습니다."
