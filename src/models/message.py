import enum

from zoneinfo import ZoneInfo
from datetime import datetime, timezone

from models import db


class MessageRole(enum.Enum):
  user = "user"
  assistant = "assistant"

# message db model - every message includes id,conversation_id(FK) role, content and created_at fields
class Message(db.Model):
  __tablename__ = "messages"

  id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
  conversation_id = db.Column(
    db.BigInteger,
    db.ForeignKey("conversations.id"),
    nullable=False,
    index=True,
  )
# adds the role of the message's creator ("user" or "assistant")
  role = db.Column(db.Enum(MessageRole), nullable=False)
# messages's text
  content = db.Column(db.Text, nullable=False)

# automatically adds the created date to a new message
  created_at = db.Column(
    db.DateTime,
    nullable=False,   
    default=lambda: datetime.now(tz = None),
    server_default=db.func.now()
    )
    
  
# defines how an object is represented as a string
  def __repr__(self):
    return f"<Message {self.role.value} in conversation {self.conversation_id}>"
