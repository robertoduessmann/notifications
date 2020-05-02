import datetime
from datetime import datetime

from ext.database import Database
from model.notification import Notification

class NotificationRepository:
    def __init__(self, db_instance: Database):
        self.__database = db_instance

    def get_notifications(self, user_id):
        query = "select id, user_id, message, is_read created_at from notifications where user_id = %s"
        return self._execute_query(query, (user_id,))

    def save_notification(self, notification: Notification):
        query = "insert into notifications ({}) values {}".format(notification.insert_projection(), notification.insert_values())
        return self._execute_query(query)

    def _execute_query(self, query: str, params=None):
        conn = self.__database.get_connection()
        cur = conn.cursor(dictionary=True)

        result = cur.execute(query) if params is None else cur.execute(query, params)

        if query.lower().startswith("select"):
            result = cur.fetchall()

        conn.commit()
        cur.close()

        return result