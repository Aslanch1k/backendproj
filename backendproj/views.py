from flask import jsonify, request
from uuid import uuid1
from backendproj import app
from datetime import datetime

user_id_counter = 0
def user_id_counter_plus_one():
    global user_id_counter
    user_id_counter += 1
    return user_id_counter

USERS = [
    {
        "User id": user_id_counter_plus_one(),
        "User name": "Oleg",
    },
    {
        "User id": user_id_counter_plus_one(),
        "User name": "Masha",
    },
    {
        "User id": user_id_counter_plus_one(),
        "User name": "Artem",
    },
]

categories_id_counter = 0
def categories_id_counter_plus_one():
    global categories_id_counter
    categories_id_counter += 1
    return categories_id_counter

CATEGORIES = [
    {
        "Category id": categories_id_counter_plus_one(),
        "Category name": "Shoes",
    },
    {
        "Category id": categories_id_counter_plus_one(),
        "Category name": "Shirts",
    },
    {
        "Category id": categories_id_counter_plus_one(),
        "Category name": "T-shirts",
    }
]

now = datetime.now()
records_id_counter = 0
def records_id_counter_plus_one():
    global records_id_counter
    records_id_counter += 1
    return records_id_counter

RECORDS = [
    {"Record id": records_id_counter_plus_one(),
     "User id": USERS[0]["User id"],
     "Category id": CATEGORIES[0]["Category id"],
     "Date and time of record": now.strftime("%d/%m/%Y %H:%M:%S"),
     "Amount of expenditure in USD": 500
     },
    {"Record id": records_id_counter_plus_one(),
     "User id": USERS[1]["User id"],
     "Category id": CATEGORIES[1]["Category id"],
     "Date and time of record": now.strftime("%d/%m/%Y %H:%M:%S"),
     "Amount of expenditure in USD": 320
     },
    {"Record id": records_id_counter_plus_one(),
     "User id": USERS[0]["User id"],
     "Category id": CATEGORIES[1]["Category id"],
     "Date and time of record": now.strftime("%d/%m/%Y %H:%M:%S"),
     "Amount of expenditure in USD": 250
     },
    {"Record id": records_id_counter_plus_one(),
     "User id": USERS[1]["User id"],
     "Category id": CATEGORIES[0]["Category id"],
     "Date and time of record": now.strftime("%d/%m/%Y %H:%M:%S"),
     "Amount of expenditure in USD": 730
     }
]


@app.route("/categories")
def get_categories():
    return jsonify({"Categories": CATEGORIES})

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

@app.route("/record", methods = ['POST'])
def create_record():
    request_data = request.get_json()
    request_data["Record id"] = records_id_counter_plus_one()
    now = datetime.now()
    request_data["Date and time of record"] = now.strftime("%d/%m/%Y %H:%M:%S")
    if (request_data["User id"] > user_id_counter) or (request_data["Category id"] > categories_id_counter):
        return IndexError
    RECORDS.append(request_data)
    print(RECORDS)
    return jsonify({"Status": "ok"})