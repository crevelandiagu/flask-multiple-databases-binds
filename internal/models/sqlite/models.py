import datetime
from extensions.database import db


class MyModleSqlite(db.Model):
    __bind_key__ = 'cache'
    __tablename__ = 'cache_memory'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(150), nullable=True)
    status: str = db.Column(db.String(150), nullable=True)
    years_exp: float = db.Column(db.Numeric, nullable=True, default=0)
    createdAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)
    updatedAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)


