from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import relationship
import uuid

@dataclass
class User(db.Model):
    user_id: uuid.UUID
    user_name: str
    user_email: str
    user_password: str

    __tablename__ = 'users'

    user_id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()), unique=True, nullable=False)
    user_name = db.Column(db.String(), nullable=False)
    user_email = db.Column(db.String(), nullable=False, unique=True)
    user_password = db.Column(db.String(), nullable=False)

    tasks = relationship('Task', backref='user', lazy=True)
