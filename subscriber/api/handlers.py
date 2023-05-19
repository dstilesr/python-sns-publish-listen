import logging
from config import SUBSCRIBER


class SubscribeHandler:

    def __init__(self):
        self.logger = logging.getLogger("subscriber")
        self.logger.setLevel(logging.INFO)

    def process(self, **kwargs):
        """
        Processes a message received from SNS.
        :param kwargs: Request arguments
        :return:
        """
        try:
            self.logger.info(f"MESSAGE RECEIVED. TYPE: {kwargs['Type']}")
            self.logger.info(kwargs["Message"])

            if kwargs['Type'] == "Notification":
                logging.info("NOTIFICATION_RECEIVED")
                # Do something interesting with the message. . .

            elif kwargs['Type'] == "SubscriptionConfirmation":
                SUBSCRIBER.confirm_subscription(kwargs["Token"])

            return True

        except Exception as e:
            self.logger.error("Subscriber fail! %s" % str(e))
            return False
