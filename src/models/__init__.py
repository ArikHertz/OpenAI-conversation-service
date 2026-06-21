from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from models.conversation import Conversation  # noqa: E402, F401
from models.message import Message  # noqa: E402, F401
