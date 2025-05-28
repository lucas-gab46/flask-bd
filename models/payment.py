from extensions import db
from datetime import datetime

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float, nullable=False)
    expiration_date = db.Column(db.DateTime, nullable=False)
    paid = db.Column(db.Boolean, default=False)
    qr_code = db.Column(db.String(255))

    def to_dict(self):
        return {
            "id": self.id,
            "value": self.value,
            "expiration_date": self.expiration_date.isoformat(),
            "paid": self.paid,
            "qr_code": self.qr_code
        }
