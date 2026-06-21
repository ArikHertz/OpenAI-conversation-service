from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

# chat box format 
class ChatForm(FlaskForm):
  content = TextAreaField(
    "Message",
    validators=[
      DataRequired(message="Please enter a message."),
      Length(max=8000, message="Message must be 8000 characters or fewer."),
    ],
    render_kw={
      "rows": 3,
      "placeholder": "Send a message...",
      "class": "form-control chat-input",
      "id": "message-input",
    },
  )
  submit = SubmitField(
    "Send",
    render_kw={"class": "btn btn-primary chat-send-btn"},
  )

# button of "new conversation" format
class NewConversationForm(FlaskForm):
  submit = SubmitField(
    "New Conversation",
    render_kw={"class": "btn btn-outline-secondary btn-sm"},
  )
