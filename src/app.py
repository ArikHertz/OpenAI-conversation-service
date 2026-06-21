from flask import Flask
from flask_wtf.csrf import CSRFProtect

from config import Config
from models import db
from routes.main import main_bp

csrf = CSRFProtect()


def create_app():
  
  # Creates the Flask application instance.
  app = Flask(__name__)

  # Loads configuration settings from a Config class.
  app.config.from_object(Config)

  # Security check:
  # If SECRET_KEY is missing → the app stops immediately
  if not app.config.get("SECRET_KEY"):
    raise ValueError("SECRET_KEY must be set in the environment or .env file.")
  
  # Connects the database to the app.
  db.init_app(app)

  # Enables CSRF protection across the entire app.
  csrf.init_app(app)

# Adds modular routes to the app.
# Instead of one big file, Flask apps are split into parts called Blueprints.
  app.register_blueprint(main_bp)
  
  # Creates an application context so Flask can access app resources.
  with app.app_context():
    # Creates all database tables defined in your models.
    db.create_all()

  return app

# creating the app
app = create_app()

# Checks if this file is being run directly. otherwise - don't run it
if __name__ == "__main__":
  app.run(debug=True)
