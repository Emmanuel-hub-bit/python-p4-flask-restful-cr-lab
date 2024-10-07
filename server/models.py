from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=True)
    price = db.Column(db.Numeric, nullable=False)  # Use Numeric for decimal values

    def __repr__(self):
        return f'{self.name}, {self.image}, {self.price}'
