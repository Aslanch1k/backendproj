from flask import jsonify, request
from backendproj import app
from datetime import datetime
from backendproj.counters import user_id_counter_plus_one, categories_id_counter_plus_one, records_id_counter_plus_one
from backendproj.sort_defs import sort_for_category, sort_user_records
from backendproj.data_file import USERS,CATEGORIES,RECORDS

@app.route("/categories")
def get_categories():
    return jsonify({"Categories": CATEGORIES})


user1 = USERS[0]


@app.route(f"/user{user1['User id']}records")
def get_user_records():
    global user1
    username = user1["User name"]
    return jsonify({f"User {username} records": sort_user_records(RECORDS, user1)})


user2 = USERS[1]
category = CATEGORIES[0]


@app.route(f"/user{user2['User id']}recordsincategory{category['Category id']}")
def get_user_records_in_category():
    global user2, category
    username = user2["User name"]
    categoryname = category["Category name"]
    return jsonify({f"User {username} records in category {categoryname}":
                        sort_for_category(category, sort_user_records(RECORDS, user2))})


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

        return IndexError
    else:
        request_data["Record id"] = records_id_counter_plus_one()
        now = datetime.now()
        request_data["Date and time of record"] = now.strftime("%d/%m/%Y %H:%M:%S")
        RECORDS.append(request_data)
        print(RECORDS)
        return jsonify({"Status": "ok"})
