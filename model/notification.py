from datetime import datetime

class Notification:
    def __init__(self, id, user_id, message, is_read=False, created_at=datetime.now()):
        self.__id = id
        self.__user_id = user_id
        self.__message = message
        self.__is_read = is_read
        self.__created_at = created_at

    def to_json(self):
        return {
            "id": self.__id,
            "user_id": self.__user_id,
            "message": str(self.__message),
            "is_read": self.__is_read,
            "created_at": str(self.__created_at)
        }

    def _is_read(self):
        is_read = self.__is_read
        return False if is_read is None or is_read == 0 else True

    def insert_values(self):
        return self.__id, \
               self.__user_id, \
               self.__message, \
               self._is_read(), \
               str(self.__created_at)

    @classmethod
    def insert_projection(cls):
        return "id, user_id, message, is_read, created_at"