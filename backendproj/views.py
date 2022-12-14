from backendproj import app
from flask_smorest import Api

from backendproj.db import db
from backendproj.resources.user import blp as UserBlueprint
from backendproj.resources.category import blp as CategoryBlueprint
from backendproj.resources.record import blp as RecordBlueprint
from backendproj.resources.currency import blp as CurrencyBlueprint

user_id_for_checking_records = 1
user_id_for_checking_records_in_category = 1
category_id_for_checking_records = 1

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Finance REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = '/swagger_ui'
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_MODIFICATIONS"] = False
db.init_app(app)

api = Api(app)

with app.app_context():
    db.create_all()

api.register_blueprint(UserBlueprint)
api.register_blueprint(CategoryBlueprint)
api.register_blueprint(RecordBlueprint)
api.register_blueprint(CurrencyBlueprint)

