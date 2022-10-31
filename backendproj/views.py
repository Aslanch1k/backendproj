from flask import jsonify, request
from backendproj import app
from datetime import datetime
from backendproj.counters import user_id_counter_plus_one, categories_id_counter_plus_one, records_id_counter_plus_one
from backendproj.sort_defs import sort_for_category, sort_user_records
from backendproj.data_file import USERS, CATEGORIES, RECORDS

user_id_for_checking_records = 1
user_id_for_checking_records_in_category = 1
category_id_for_checking_records = 1


@app.route("/categories")
def get_categories():
    return jsonify({"Categories": CATEGORIES})


@app.route("/userrecords", methods=['POST'])
def check_user_id_for_get_it():
    global user_id_for_checking_records
    userdata = request.get_json()
    if userdata["User id"] <= len(USERS):
        user_id_for_checking_records = userdata["User id"]
        return jsonify({"Status": "ok"})
    else:
        return jsonify({"Status": "User does not exist"})


@app.route("/userrecordsincategory", methods=['POST'])
def check_user_and_category_id_for_get_it():
    global user_id_for_checking_records_in_category, category_id_for_checking_records
    user_and_category_data = request.get_json()
    if (user_and_category_data["User id"] <= len(USERS)) and (user_and_category_data["Category id"] <= len(CATEGORIES)):
        user_id_for_checking_records_in_category = user_and_category_data["User id"]
        category_id_for_checking_records = user_and_category_data["Category id"]
        return jsonify({"Status": "ok"})
    else:
        return jsonify({"Status": "User or category does not exist"})


@app.route(f"/userrecordsbyid")
def get_user_records():
    user = USERS[user_id_for_checking_records - 1]
    username = user["User name"]
    userid = user["User id"]
    return jsonify({f"User name: {username} | "
                    f"User id: {userid} | "
                    f"User records": sort_user_records(RECORDS, user)})


@app.route(f"/userrecordsincategory")
def get_user_records_in_category():
    user = USERS[user_id_for_checking_records_in_category - 1]
    category = CATEGORIES[category_id_for_checking_records - 1]
    username = user["User name"]
    userid = user["User id"]
    categoryid = category["Category id"]
    categoryname = category["Category name"]
    return jsonify({f"User name: {username} | "
                    f"User id: {userid} | "
                    f"Category: {categoryname} | "
                    f"Category id: {categoryid} | "
                    f"Users records in category: ": sort_for_category(category, sort_user_records(RECORDS, user))})


@app.route("/category", methods=['POST'])
def create_category():
    request_data = request.get_json()
    request_data["Category id"] = categories_id_counter_plus_one()
    CATEGORIES.append(request_data)
    print(CATEGORIES)
    return jsonify({"Status": "ok"})


@app.route("/user", methods=['POST'])
def create_user():
    request_data = request.get_json()
    request_data["User id"] = user_id_counter_plus_one()
    USERS.append(request_data)
    print(USERS)
    return jsonify({"Status": "ok"})


@app.route("/record", methods=['POST'])
def create_record():
    request_data = request.get_json()
    if (request_data["User id"] > USERS[-1]["User id"]) or \
            (request_data["Category id"] > CATEGORIES[-1]["Category id"]):
        return jsonify({"Status": "User does not exist"})
    else:
        request_data["Record id"] = records_id_counter_plus_one()
        now = datetime.now()
        request_data["Date and time of record"] = now.strftime("%d/%m/%Y %H:%M:%S")
        RECORDS.append(request_data)
        print(RECORDS)
        return jsonify({"Status": "ok"})
