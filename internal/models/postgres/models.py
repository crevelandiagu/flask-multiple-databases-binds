import datetime
from sqlalchemy.dialects.postgresql import JSONB
from extensions.database import db


class MyModelPostgres(db.Model):

    __tablename__ = 'otro'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data = db.Column(JSONB, nullable=True)
    createdAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)
    updatedAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)
