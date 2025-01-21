# Correct database URL for SQLite
import os


SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./social_app.db")
