import os

class Config:
    """Base configuration for the application."""
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///math_operations.db")  # Default to SQLite for local dev
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DEV_DATABASE_URL", "sqlite:///math_operations.db")  # Local dev DB

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")  # Uses Render's PostgreSQL

# Select the config based on environment variable
ENV = os.getenv("FLASK_ENV", "development")  # Default to development
CurrentConfig = config.get(ENV, DevelopmentConfig)
