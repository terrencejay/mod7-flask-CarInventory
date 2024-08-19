import os
from dotenv import load_dotenv
from supabase import create_client, Client

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    '''
    Set config variables for the Flask app
    Using Environment variables where available.
    Otherwise create the config variable if not done already
    '''
    load_dotenv()  # Load environment variables from .env file

    FLASK_APP = os.getenv('FLASK_APP', 'app')
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')  

    url: str = os.environ.get("https://aaezxtxbrpkbhxiuhlhg.supabase.co")
    key: str = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFhZXp4dHhicnBrYmh4aXVobGhnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjIyNjkwODEsImV4cCI6MjAzNzg0NTA4MX0.qMfUuNwoaC24CWuHd6dA-nX8TxOMB6aCsrpqBXmKm2I")
    supabase: Client = create_client(url, key)

    # Use Supabase credentials for SQLAlchemy
    SUPABASE_URL = os.getenv('https://aaezxtxbrpkbhxiuhlhg.supabase.co')
    SUPABASE_KEY = os.getenv('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFhZXp4dHhicnBrYmh4aXVobGhnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjIyNjkwODEsImV4cCI6MjAzNzg0NTA4MX0.qMfUuNwoaC24CWuHd6dA-nX8TxOMB6aCsrpqBXmKm2I')
    
    # Construct the SQLAlchemy database URL using Supabase credentials
    SQLALCHEMY_DATABASE_URL = os.getenv('postgresql://postgres.aaezxtxbrpkbhxiuhlhg:13PinOak29!@aws-0-us-west-1.pooler.supabase.com:6543/postgres') or f'postgresql://postgres:{SUPABASE_KEY}@{SUPABASE_URL}/postgres'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
