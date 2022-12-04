from sqlalchemy.exc import IntegrityError
from flask_smorest import Blueprint
from flask.views import MethodView
from flask_smorest import abort
from backendproj.db import db
from backendproj.models.user import UserModel
from backendproj.schemas import UserSchema

blp = Blueprint("user", __name__, description="Operations on user")


@blp.route("/user/<string:user_id>")
class User(MethodView):

    @blp.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user


@blp.route("/user")
class UserList(MethodView):

    @blp.response(200, UserSchema(many=True))
    def get(self):
        return UserModel.query.all()

    @blp.arguments(UserSchema)
    @blp.response(200, UserSchema)
    def post(self, user_data):
        if "currency_id" not in user_data:
            user_data["currency_id"] = 1
        user = UserModel(**user_data)
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="User with this name already exists"
            )
        return user