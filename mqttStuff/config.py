import os

class Config:
    """Base configuration class."""
    # Secret key for session management and CSRF protection
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_default_secret_key'  # Change this to a strong secret key

    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://root:your_mysql_password@localhost/iotclients_database'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable track modifications to save resources

class DevelopmentConfig(Config):
    """Development configuration class."""
    DEBUG = True  # Enable debug mode for development
    # Add any other development-specific configurations here

class ProductionConfig(Config):
    """Production configuration class."""
    DEBUG = False  # Disable debug mode in production
    # Add any other production-specific configurations here
