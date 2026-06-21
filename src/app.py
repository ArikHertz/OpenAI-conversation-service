from flask import Flask
from flask_wtf.csrf import CSRFProtect

from config import Config
from models import db
from routes.main import main_bp

csrf = CSRFProtect()


def create_app():
  app = Flask(__name__)
  app.config.from_object(Config)

  if not app.config.get("SECRET_KEY"):
    raise ValueError("SECRET_KEY must be set in the environment or .env file.")

  db.init_app(app)
  csrf.init_app(app)
  app.register_blueprint(main_bp)

  with app.app_context():
    db.create_all()

  return app


app = create_app()


if __name__ == "__main__":
  app.run(debug=True)
