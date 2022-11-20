from flask_smorest import Blueprint
from flask.views import MethodView
from flask_smorest import abort
from backendproj.counters import user_id_counter_plus_one
from backendproj.data_file import USERS
from flask import request

blp = Blueprint("user", __name__, description="Operations on user")


@blp.route("/user/<string:user_id>")
class User(MethodView):
    def get(self, user_id):
        user_id = int(user_id)
        try:
            return USERS[user_id]
        except KeyError:
            abort(404, message="User not found")

    def delete(self, user_id):
        user_id = int(user_id)
        try:
            deleted_user = USERS[user_id]
            del USERS[user_id]
            return deleted_user
        except KeyError:
            abort(404, message="User not found")


@blp.route("/user")
class UserList(MethodView):
    def get(self):
        return USERS

    def post(self):
        request_data = request.get_json()
        if "User name" not in request_data:
            abort(400, message="Need name for creating user")
        if request_data["User name"] in [u["User name"] for u in USERS]:
            abort(400, message="Name must be unique")
        request_data["User id"] = user_id_counter_plus_one()
        USERS.append(request_data)
        return request_data
