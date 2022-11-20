from backendproj import app
from flask_smorest import abort, Api
from backendproj.resources.user import blp as UserBlueprint
from backendproj.resources.category import blp as CategoryBlueprint
from backendproj.resources.record import blp as RecordBlueprint

user_id_for_checking_records = 1
user_id_for_checking_records_in_category = 1
category_id_for_checking_records = 1

app.config["PROPAGATE_EXCEPTIONS"]=True
app.config["API_TITLE"]="Finance REST API"
app.config["API_VERSION"]="v1"
app.config["OPENAPI_VERSION"]="3.0.3"
app.config["OPENAPI_URL_PREFIX"]="/"
app.config["OPENAPI_SWAGGER_UI_PATH"]='/swagger_ui'
app.config["OPENAPI_SWAGGER_UI_URL"]="https://cdn.jsdelivr.net/npm/swagger-ui-dist"

api = Api(app)
api.register_blueprint(UserBlueprint)
api.register_blueprint(CategoryBlueprint)
api.register_blueprint(RecordBlueprint)
