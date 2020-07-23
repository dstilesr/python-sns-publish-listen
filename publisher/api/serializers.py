from pydantic import BaseModel


class Serializer(BaseModel):
    """
    Request to publish message to SNS
    """
    message: str
