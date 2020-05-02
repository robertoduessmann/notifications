from repository.notification import NotificationRepository
from model.notification import Notification
import math


class NotificationService:
    def __init__(self, notification_rep: NotificationRepository):
        self.__notification_rep = notification_rep

    def get_notifications(self, user_id):
        result = self.__notification_rep.get_notifications(user_id)
        return self._build_Notification_list(result)

    def save_notification(self, data):
        notification = Notification(**data)
        self.__notification_rep.save_notification(notification)
        return notification.to_json()

    def _build_Notification_list(self, result):
        notification_list = []
        for notification in result:
            notification_list.append(Notification(**notification).to_json())
        return notification_list