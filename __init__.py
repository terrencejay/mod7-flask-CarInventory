from flask import Flask

from .config import Config
from .site.routes import site
from .authentication.routes import auth
from .api.routes import api
from supabase import create_client, Client
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db as root_db, login_manager, ma
from flask_cors import CORS
from helpers import JSONEncoder

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configure Supabase
SUPABASE_URL = os.getenv('https://aaezxtxbrpkbhxiuhlhg.supabase.co')
SUPABASE_KEY = os.getenv('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFhZXp4dHhicnBrYmh4aXVobGhnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjIyNjkwODEsImV4cCI6MjAzNzg0NTA4MX0.qMfUuNwoaC24CWuHd6dA-nX8TxOMB6aCsrpqBXmKm2I')
url: str = os.environ.get("https://aaezxtxbrpkbhxiuhlhg.supabase.co")
key: str = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFhZXp4dHhicnBrYmh4aXVobGhnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjIyNjkwODEsImV4cCI6MjAzNzg0NTA4MX0.qMfUuNwoaC24CWuHd6dA-nX8TxOMB6aCsrpqBXmKm2I")
supabase: Client = create_client(url, key)

# Configure Flask app
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')  

# Initialize extensions
root_db.init_app(app)
login_manager.init_app(app)
ma.init_app(app)
migrate = Migrate(app, root_db)

# Register blueprints
app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)

# Set custom JSON encoder
app.json_encoder = JSONEncoder

if __name__ == '__main__':
    app.run(debug=True)
