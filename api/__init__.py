from flask import Flask
from flask_mysqldb import MySQL

# Initialize Flask extensions
mysql = MySQL()

def create_app():
    """Create and configure the Flask app."""
    app = Flask(__name__)

    # Database configuration (update with your credentials)
    app.config['MYSQL_HOST'] = 'db'  # Use 'db' if using Docker, else 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'your_password'
    app.config['MYSQL_DB'] = 'travel_company'
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'  # Return results as dictionaries

    # Initialize extensions
    mysql.init_app(app)

    # Register Blueprints
    from .blueprints.clients import clients_bp
    from .blueprints.travel_packages import packages_bp
    from .blueprints.flights import flights_bp
    from .blueprints.travel_agents import agents_bp

    app.register_blueprint(clients_bp)
    app.register_blueprint(packages_bp)
    app.register_blueprint(flights_bp)
    app.register_blueprint(agents_bp)

    return app
