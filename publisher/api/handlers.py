import os
import json
import boto3
from datetime import datetime


class PublishHandler(object):

    MAX_LEN: int = 1000  #: Maximum message length for publishing

    @classmethod
    def publish_message_sns(cls, message: str) -> bool:
        """
        Publishes messages to SNS.

        :param message:
        :return: True if successful, false if not.
        """
        try:
            output = {
                "message_length": len(message),
                "received_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
                "message": message[:cls.MAX_LEN]
            }

            sns = boto3.client(
                "sns",
                aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
                aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
                region_name=os.getenv("AWS_REGION")
            )
            sns.publish(
                TopicArn=os.getenv("SNS_TOPIC"),
                Message=json.dumps(output)
            )
            return True

        except Exception as e:
            print(e)
            return False

    @classmethod
    def process(cls, message: str):
        return cls.publish_message_sns(message)
