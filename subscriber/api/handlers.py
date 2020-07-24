import logging
from config import SUBSCRIBER


class SubscribeHandler(object):

    @classmethod
    def process(cls, **kwargs):
        """
        Processes a message received from SNS.

        :param kwargs: Request arguments
        :return:
        """
        try:
            logging.info(f"MESSAGE RECEIVED. TYPE: {kwargs['Type']}")
            print(kwargs["Message"])

            if kwargs['Type'] == "Notification":
                logging.info("NOTIFICATION_RECEIVED")
                # Do something interesting with the message. . .

            elif kwargs['Type'] == "SubscriptionConfirmation":
                SUBSCRIBER.confirm_subscription(kwargs["Token"])

            return True

        except Exception as e:
            print(e)
            return False
