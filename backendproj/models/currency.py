from backendproj.db import db


class CurrencyModel(db.Model):
    __tablename__ = "currency"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    currency_to_usd = db.Column(db.Float, nullable=False)

    user = db.relationship(
        "UserModel",
        back_populates="currency",
        lazy="dynamic",
    )
