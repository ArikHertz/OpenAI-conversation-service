from datetime import datetime, timezone

from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from forms.chat_forms import ChatForm, NewConversationForm
from models import db
from models.conversation import Conversation
from models.message import Message, MessageRole
from services.openai_service import get_assistant_reply

main_bp = Blueprint("main", __name__)

# returns the list of a conversation from the DB according to its id. if there is no such a conversation, returns an empty array
def _load_messages(conversation_id):
  if not conversation_id:
    return []

  return (
    Message.query.filter_by(conversation_id=conversation_id)
    .order_by(Message.created_at.asc())
    .all()
  )

# returns the conversation DB details if there is an active conversation in the current session.
# if there is no conversation, creating a new conversation and adding to DB.
def _get_or_create_conversation():
  conversation_id = session.get("conversation_id")

  if conversation_id:
    conversation = Conversation.query.get(conversation_id)
    if conversation:
      return conversation

  conversation = Conversation()

  db.session.add(conversation)
  db.session.commit()


  return conversation


@main_bp.route("/", methods=["GET", "POST"])
def home():
  chat_form = ChatForm()
  new_conversation_form = NewConversationForm()

  if request.method == "GET":
    keep = session.pop("_keep_conversation", False)
    if not keep:
      session.pop("conversation_id", None)
    if keep is False and "conversation_id" not in session:
        session.pop("conversation_id", None)

    conversation_id = session.get("conversation_id")

    messages = _load_messages(conversation_id)
    return render_template(
      "home.html",
      chat_form=chat_form,
      new_conversation_form=new_conversation_form,
      messages=messages,
    )

  if not chat_form.validate_on_submit():
    for field_errors in chat_form.errors.values():
      for error in field_errors:
        flash(error, "danger")
    return redirect(url_for("main.home"))

  content = (chat_form.content.data or "").strip()
  if not content:
    flash("Please enter a message.", "danger")
    return redirect(url_for("main.home"))

  try:

    # getting the current conversation's messages if there is a conversation_id in the current session.
    # if not, creating a new conversation.
    conversation = _get_or_create_conversation()

    # creating a Message object from the user line.
    user_message = Message(
      conversation_id=conversation.id, # type: ignore
      role=MessageRole.user, # type: ignore
      content=content, # type: ignore
    )
    # adding the message into the DB
    db.session.add(user_message)
    db.session.commit()

    # getting the assistant reply
    get_assistant_reply(conversation.id)

    # updates the session
    session["conversation_id"] = conversation.id
    session["_keep_conversation"] = True
    return redirect(url_for("main.home"))
  except Exception as e:
    # if the action fails, write a message to the user in the browser, and the exact error in the terminal
    db.session.rollback()
    flash(
      "Something went wrong while processing your message. Please try again.",
      "danger",
    )
    print("❌ ERROR:", repr(e))

    
    return redirect(url_for("main.home"))

# routes to the "about" page according to the user's choice
@main_bp.route("/about")
def about():
  return render_template("about.html")

# opening a new conversation
@main_bp.route("/new-conversation", methods=["POST"])
def new_conversation():
  new_conversation_form = NewConversationForm()
  
  # when the request fails from any reason - writing a suitable message and redirecting to home page
  if not new_conversation_form.validate_on_submit():
    flash("Invalid request. Please try again.", "danger")
    return redirect(url_for("main.home"))

  try:
    # creating a new conversation and write it in the DB
    conversation = Conversation()
    db.session.add(conversation)
    db.session.commit()

    # updates the current sessin
    session["conversation_id"] = conversation.id
    session["_keep_conversation"] = True
    flash("Started a new conversation.", "success")
    return redirect(url_for("main.home"))
  except Exception:
    # updates the user if the conversation failed to be created and redirect to home page
    db.session.rollback()
    flash("Could not start a new conversation. Please try again.", "danger")
    return redirect(url_for("main.home"))
