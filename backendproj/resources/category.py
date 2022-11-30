import flask
from flask_smorest import Blueprint
from flask.views import MethodView
from flask_smorest import abort
from backendproj.db import db
from sqlalchemy.exc import IntegrityError

from backendproj.models import CategoryModel
from backendproj.schemas import CategorySchema

blp = Blueprint("category", __name__, description="Operations on category")


@blp.route("/category/<string:category_id>")
class Category(MethodView):

    @blp.response(200, CategorySchema)
    def get(self, category_id):
        category = CategoryModel.query.get_or_404(category_id)
        return category

    # def delete(self, category_id):
    #     category_id = int(category_id)
    #     try:
    #         deleted_category = CATEGORIES[category_id]
    #         del CATEGORIES[category_id]
    #         return deleted_category
    #     except KeyError:
    #         abort(404, message="Category not found")


@blp.route("/category")
class CategoryList(MethodView):

    @blp.response(200, CategorySchema(many=True))
    def get(self):
        return CategoryModel.query.all()

    @blp.arguments(CategorySchema)
    @blp.response(200,CategorySchema)
    def post(self, category_data):
        category = CategoryModel(**category_data)
        try:
            db.session.add(category)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="Category with this name already exists"
            )
        return category

