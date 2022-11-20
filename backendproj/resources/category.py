from flask_smorest import Blueprint
from flask.views import MethodView
from flask_smorest import abort
from backendproj.counters import categories_id_counter_plus_one
from backendproj.data_file import CATEGORIES
from flask import request

blp = Blueprint("category", __name__, description="Operations on category")


@blp.route("/category/<string:category_id>")
class Category(MethodView):
    def get(self, category_id):
        category_id = int(category_id)
        try:
            return CATEGORIES[category_id]
        except KeyError:
            abort(404, message="Category not found")

    def delete(self, category_id):
        category_id = int(category_id)
        try:
            deleted_category = CATEGORIES[category_id]
            del CATEGORIES[category_id]
            return deleted_category
        except KeyError:
            abort(404, message="Category not found")


@blp.route("/category")
class CategoryList(MethodView):
    def get(self):
        return CATEGORIES

    def post(self):
        request_data = request.get_json()
        if "Category name" not in request_data:
            abort(400, message="Need category name for creating category")
        if request_data["Category name"] in [u["Category name"] for u in CATEGORIES]:
            abort(400, message="Category name must be unique")
        request_data["Category id"] = categories_id_counter_plus_one()
        CATEGORIES.append(request_data)
        return request_data

