from app.configs.database import db
from dataclasses import dataclass
import uuid

@dataclass
class Task(db.Model):
    task_id: uuid.UUID
    task_content: str

    __tablename__ = 'tasks'

    task_id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()), unique=True, nullable=False)
    task_content = db.Column(db.String(), nullable=False)

    user_id = db.Column(db.String(36), db.ForeignKey('users.user_id'), nullable=False)
