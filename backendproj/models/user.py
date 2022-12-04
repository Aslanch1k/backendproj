from backendproj.db import db


class UserModel(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    currency_id = db.Column(
        db.Integer,
        db.ForeignKey("currency.id"),
        unique=False,
        nullable=False
    )

    currency = db.relationship("CurrencyModel", back_populates="user")

    record = db.relationship(
        "RecordModel",
        back_populates="user",
        lazy="dynamic",
    )
