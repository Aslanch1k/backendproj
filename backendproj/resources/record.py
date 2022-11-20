from flask_smorest import Blueprint
from flask.views import MethodView
from flask_smorest import abort
from backendproj.counters import records_id_counter_plus_one
from backendproj.data_file import RECORDS, USERS, CATEGORIES
from flask import request
from datetime import datetime

from backendproj.sort_defs import sort_user_records, sort_for_category

blp = Blueprint("record", __name__, description="Operations on record")


@blp.route("/record/<string:record_id>")
class Record(MethodView):
    def get(self, record_id):
        record_id = int(record_id)
        try:
            return RECORDS[record_id]
        except KeyError:
            abort(404, message="Record not found")

    def delete(self, record_id):
        record_id = int(record_id)
        try:
            deleted_record = RECORDS[record_id]
            del RECORDS[record_id]
            return deleted_record
        except KeyError:
            abort(404, message="Record not found")


@blp.route("/record")
class RecordList(MethodView):
    def get(self):
        return RECORDS

    def post(self):
        request_data = request.get_json()
        if (
                "User id" not in request_data
                or "Category id" not in request_data
                or "Amount of expenditure in USD" not in request_data
        ):
            abort(400, message="There are no user or category id or no amount of expenditure in "
                               "USD for creating record")
        if (request_data["User id"] not in [u["User id"] for u in USERS]) or \
                (request_data["Category id"] not in [u["Category id"] for u in CATEGORIES]):
            abort(400, message="There are no category or user with such id")
        if request_data["Amount of expenditure in USD"] <= 0:
            abort(400, message="Amount of expenditure can't be less than 0")
        request_data["Record id"] = records_id_counter_plus_one()
        now = datetime.now()
        request_data["Date and time of record"] = now.strftime("%d/%m/%Y %H:%M:%S")
        RECORDS.append(request_data)
        return request_data


@blp.route("/record/user/<string:user_id>")
class UsersRecordList(MethodView):
    def get(self, user_id):
        user_id = int(user_id)
        if user_id not in [u["User id"] for u in USERS]:
            abort(400, message="There are no user with such id")
        user = USERS[user_id]
        username = user["User name"]
        userid = user["User id"]
        return {f"User name: {username} | "
                f"User id: {userid} | "
                f"User records": sort_user_records(RECORDS, user)}


@blp.route("/record/user/<string:user_id>/category/<string:category_id>")
class UserRecordListInCategory(MethodView):
    def get(self, user_id, category_id):
        user_id = int(user_id)
        category_id = int(category_id)
        if (user_id not in [u["User id"] for u in USERS]) or \
                (category_id not in [u["Category id"] for u in CATEGORIES]):
            abort(400, message="There are no category or user with such id")
        user = USERS[user_id]
        category = CATEGORIES[category_id]
        username = user["User name"]
        userid = user["User id"]
        categoryid = category["Category id"]
        categoryname = category["Category name"]
        return {f"User name: {username} | "
                f"User id: {userid} | "
                f"Category: {categoryname} | "
                f"Category id: {categoryid} | "
                f"Users records in category: ": sort_for_category(category, sort_user_records(RECORDS, user))}
