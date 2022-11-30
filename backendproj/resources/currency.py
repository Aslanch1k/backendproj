from sqlalchemy.exc import IntegrityError
from flask_smorest import Blueprint
from flask.views import MethodView
from flask_smorest import abort
from backendproj.db import db
from backendproj.models.currency import CurrencyModel
from backendproj.models.user import UserModel
from backendproj.schemas import UserSchema, CurrencySchema
import backendproj.currency as cur

blp = Blueprint("currency", __name__, description="Operations on currency")


@blp.route("/currency/<string:currency_id>")
class Currency(MethodView):
    @blp.response(200, CurrencySchema)
    def get(self, currency_id):
        currency = CurrencyModel.query.get_or_404(currency_id)
        return currency


@blp.route("/currency")
class CurrencyList(MethodView):

    @blp.response(200, CurrencySchema(many=True))
    def get(self):
        return CurrencyModel.query.all()

    @blp.arguments(CurrencySchema)
    @blp.response(200, CurrencySchema)
    def post(self, currency_data):
        currency_convert = cur.Currency(currency_data["name"])
        currency_data["currency_to_usd"] = currency_convert.return_currency_to_USD()
        currency = CurrencyModel(**currency_data)
        try:
            db.session.add(currency)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="This currency already exists"
            )
        return currency
