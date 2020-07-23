from . import handlers
from starlette import status
from fastapi import APIRouter
from .serializers import Serializer
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/healthcheck")
async def health():
    response = JSONResponse(
        content="OK!",
        status_code=status.HTTP_200_OK
    )
    return response


@router.post("/publish-message")
async def publish_view(request: Serializer):
    """
    Receives a request to publish a message to SNS.

    :param request:
    :return:
    """
    handler = handlers.PublishHandler()
    success = handler.process(request.message)

    if success:
        response = JSONResponse(
            content={"message": "Message published successfully!"},
            status_code=status.HTTP_200_OK
        )
    else:
        response = JSONResponse(
            content={"message": "Could not publish message!"},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return response
