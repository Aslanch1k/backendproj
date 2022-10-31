def sort_for_category(category, records):
    category_records = []
    for record in records:
        if category["Category id"] == record["Category id"]:
            category_records.append(record)
    return category_records


def sort_user_records(records, user):
    user_records = []
    for record in records:
        if record["User id"] == user["User id"]:
            user_records.append(record)
    return user_records
