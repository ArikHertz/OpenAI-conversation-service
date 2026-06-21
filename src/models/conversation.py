import uuid
from datetime import datetime, timezone

from models import db

# conversation DB model. every conversations includes id, converstion_uuid and created_at fields.
class Conversation(db.Model):
  __tablename__ = "conversations"

  id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
#   makes a Universally Unique Identifier  to every conversation
  conversation_uuid = db.Column(
    db.String(36),
    unique=True,
    nullable=False,
    default=lambda: str(uuid.uuid4()),
    index=True,
  )
# automatically adds the created date to a new conversation
  created_at = db.Column(
    db.DateTime,
    nullable=False,
    default=lambda: datetime.now(tz = None),
  )
#   indictaes that current model has a one-to-many relationship with "message"
  messages = db.relationship(
    "Message",
    backref="conversation",
    lazy="dynamic",
    order_by="Message.created_at",
    cascade="all, delete-orphan",
  )
# defines how an object is represented as a string
  def __repr__(self):
    return f"<Conversation {self.conversation_uuid}>"
