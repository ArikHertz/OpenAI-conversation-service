import os
from urllib.parse import quote_plus

from dotenv import load_dotenv

load_dotenv()


class Config:
  SECRET_KEY = os.environ.get("SECRET_KEY")
  OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
  OPENAI_MODEL = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")

  MYSQL_HOST = os.environ.get("MYSQL_HOST", "localhost")
  MYSQL_PORT = os.environ.get("MYSQL_PORT", "3306")
  MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE", "chatgpt_flask")
  MYSQL_USER = os.environ.get("MYSQL_USER", "root")
  MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "")

  SQLALCHEMY_DATABASE_URI = (
    f"mysql+pymysql://{quote_plus(MYSQL_USER)}:{quote_plus(MYSQL_PASSWORD)}"
    f"@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset=utf8mb4"
  )
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  WTF_CSRF_ENABLED = True
