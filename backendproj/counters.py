user_id_counter = 0

def user_id_counter_plus_one():
    global user_id_counter
    user_id_counter += 1
    return user_id_counter


categories_id_counter = 0

def categories_id_counter_plus_one():
    global categories_id_counter
    categories_id_counter += 1
    return categories_id_counter


records_id_counter = 0

def records_id_counter_plus_one():
    global records_id_counter
    records_id_counter += 1
    return records_id_counter