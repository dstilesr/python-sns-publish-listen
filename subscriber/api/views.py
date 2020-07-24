from . import handlers
from starlette import status
from fastapi import APIRouter
from .serializers import ReceiverSerializer
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/healthcheck")
async def health():
    response = JSONResponse(
        content="OK!",
        status_code=status.HTTP_200_OK
    )
    return response


@router.post("/receive-message")
async def receive_view(request: ReceiverSerializer):
    """
    Receives a message from SNS.

    :param request:
    :return:
    """
    handler = handlers.SubscribeHandler()
    success = handler.process(**dict(request))

    if success:
        response = JSONResponse(
            content={"message": "Message received!"},
            status_code=status.HTTP_200_OK
        )
    else:
        response = JSONResponse(
            content={"message": "ERROR"},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return response
