import logging

from flask import current_app
from openai import OpenAI

from models import db
from models.message import Message, MessageRole

logger = logging.getLogger(__name__)


def get_assistant_reply(conversation_id: int) -> str:
  # getting all messages from the current conversation from the DB
  messages = (
    Message.query.filter_by(conversation_id=conversation_id)
    .order_by(Message.created_at.asc())
    .all()
  )
  # creating a messages array for the use of the AI LLM
  openai_messages = [
    {"role": message.role.value, "content": message.content}
    for message in messages
  ]
  # trying to create an assistant message
  try:
    client = OpenAI(api_key=current_app.config["OPENAI_API_KEY"])
    
    # creating the assistant response according to previous conversation's messages
    response = client.chat.completions.create(
      model=current_app.config["OPENAI_MODEL"],
      messages=openai_messages, # type: ignore
    )
    assistant_content = response.choices[0].message.content or ""
  # if the message couldn't be created - throwing an error
  except Exception as exc:
    logger.exception("OpenAI API request failed: %s", exc)
    raise
  
  # converting the assistant message to a Massege object
  assistant_message = Message(
    conversation_id=conversation_id, #  type: ignore
    role=MessageRole.assistant, #  type: ignore
    content=assistant_content, #  type: ignore
  )

  # writing the message in the DB
  db.session.add(assistant_message)
  db.session.commit()
  
  # returns the assistent message
  return assistant_content
