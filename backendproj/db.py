from backendproj.counters import user_id_counter_plus_one, categories_id_counter_plus_one, records_id_counter_plus_one, \
    user_id_counter, categories_id_counter, records_id_counter
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()