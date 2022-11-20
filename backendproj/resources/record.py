from flask_smorest import Blueprint
from flask.views import MethodView
from flask_smorest import abort
from backendproj.db import db
from sqlalchemy.exc import IntegrityError

from backendproj.models import RecordModel
from backendproj.schemas import RecordSchema, RecordQuerySchema

blp = Blueprint("record", __name__, description="Operations on record")


@blp.route("/record/<string:record_id>")
class Record(MethodView):
    @blp.response(200, RecordSchema)
    def get(self, record_id):
        record = RecordModel.query.get_or_404(record_id)
        return record

    # def delete(self, record_id):
    #     record_id = int(record_id)
    #     try:
    #         deleted_record = RECORDS[record_id]
    #         del RECORDS[record_id]
    #         return deleted_record
    #     except KeyError:
    #         abort(404, message="Record not found")


@blp.route("/record")
class RecordList(MethodView):

    @blp.arguments(RecordQuerySchema, location="query", as_kwargs=True)
    @blp.response(200, RecordSchema(many=True))
    def get(self, **kwargs):
        user_id = kwargs.get("user_id")

        if not user_id:
            return abort(400, message="Need at least user id to get record")

        if user_id:
            query = db.session.query(RecordModel).filter_by(user_id=user_id)

        category_id = kwargs.get("category_id")

        if category_id:
            query = db.session.query(RecordModel).filter_by(user_id=user_id).filter_by(category_id=category_id)

        return query.all()

    @blp.arguments(RecordSchema)
    @blp.response(200, RecordSchema)
    def post(self, record_data):
        record = RecordModel(**record_data)
        try:
            db.session.add(record)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="Error while creating record"
            )
        return record
