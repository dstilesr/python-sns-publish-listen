import os
import json
import boto3
import logging
from datetime import datetime


class PublishHandler:

    MAX_LEN: int = 1000  #: Maximum message length for publishing

    def __init__(self):
        self.logger = logging.getLogger("publisher")
        self.logger.setLevel(logging.INFO)

    def publish_message_sns(self, message: str) -> bool:
        """
        Publishes messages to SNS.
        :param message:
        :return: True if successful, false if not.
        """
        try:
            output = {
                "message_length": len(message),
                "received_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
                "message": message[:self.MAX_LEN]
            }

            sns = boto3.client(
                "sns",
                aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
                aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
                region_name=os.getenv("AWS_REGION")
            )
            self.logger.info(
                "Message to send to SNS: '%s'"
                % json.dumps(output)
            )
            sns.publish(
                TopicArn=os.getenv("SNS_TOPIC"),
                Message=json.dumps(output)
            )
            self.logger.info("Successfully sent message!")
            return True

        except Exception as e:
            self.logger.error(
                "Failed to send message! Error (%s): %s"
                % (type(e).__name__, str(e))
            )
            return False

    def process(self, message: str) -> bool:
        return self.publish_message_sns(message)
