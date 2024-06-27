from ccs.ccs import db
from datetime import datetime

class ExchangeRate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    base_currency = db.Column(db.String(3), nullable=False)
    target_currency = db.Column(db.String(3), nullable=False)
    rate = db.Column(db.Float, nullable=False)
    last_updated = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f'<ExchangeRate {self.base_currency}/{self.target_currency}: {self.rate}>'