from pydantic import BaseModel


class ReceiverSerializer(BaseModel):
    """
    Request to publish message to SNS
    """
    Type: str = "Notification"
    Token: str = ""
    SubscribeURL: str = ""
    MessageId: str
    Message: str
