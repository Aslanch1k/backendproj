from backendproj.counters import user_id_counter_plus_one, categories_id_counter_plus_one, records_id_counter_plus_one
from datetime import datetime


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