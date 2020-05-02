from flask import Flask, request
from flask_restful import Resource, Api, reqparse

from ext import database, configuration
from repository.notification import NotificationRepository
from service.notification import NotificationService
from ext import database, configuration


app = Flask(__name__)
configuration.init_app(app)
api_v1 = Api(app, "/api/v1")

db = database.Database(app.config)
rep = NotificationRepository(db)
notification_service = NotificationService(rep)

class NotificationResource(Resource):
    params = reqparse.RequestParser()
    params.add_argument("id", type=str, required=True, help="Missing required parameter")
    params.add_argument("user_id", type=str, required=True, help="Missing required parameter")
    params.add_argument("message", type=str, required=True, help="Missing required parameter")

    def get(self, user_id):
        try:
            return notification_service.get_notifications(user_id)

        except Exception as err:
            print("Internal Error: ", err)
            ex = {"message": "An error occurred while trying to fetch a Notification"}, 500

        return ex

    def post(self):
        content_type = request.content_type
        if not content_type or content_type != 'application/json':
            return "Unsupported Media Type, required 'application/json'", 415

        data = NotificationResource.params.parse_args()
        try:
            return notification_service.save_notification(data), 201
        except Exception as err:
            print("Internal Error: ", err)
            return {"message": "An error occurred while trying to save a Notification"}, 500


api_v1.add_resource(NotificationResource, "/notifications", "/notifications/<user_id>")

if __name__ == "__main__":
    app.run("0.0.0.0", 80, True)