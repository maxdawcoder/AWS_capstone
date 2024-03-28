from flask import Flask
from flask_cors import CORS
from config import DevelopmentConfig, ProductionConfig
import os

app = None

def get_or_create_app():
    # Get or create the Flask app.
    global app

    # Return the existing app if it exists.
    if app:
        return app
    
    # Create a new app instance.
    app = Flask(__name__)
    CORS(app, origins=['http://localhost:8000'])

    # Set the secret key for the app. This is used for session management.
    app.secret_key = os.urandom(16)

    # Determine configuration type and load appropriate configuration.
    # Here, we use the 'FLASK_ENV' environment variable to determine
    # the configuration type. If the environment variable is not set,
    # we default to 'development'.
    config_type = os.getenv('FLASK_ENV', 'development')
    if config_type == 'production':
        # Load production configuration.
        app.config.from_object(ProductionConfig)
        if app.config['SQLALCHEMY_DATABASE_URI'] is None:
            raise EnvironmentError('Production database URI is not configured')
    elif config_type == 'development':
        # Load development configuration.
        app.config.from_object(DevelopmentConfig)
    else:
        raise EnvironmentError(f"Unsupported 'FLASK_ENV' environment variable: {config_type}")
    
    # Import the database module and initialize it.
    from app.models import db

    # Initialize the database.
    db.init_app(app)

    # Create the database tables if they do not exist.
    with app.app_context():
        db.create_all()
    
    # Import the routes module and register the routes.
    from app import routes
    
    return app