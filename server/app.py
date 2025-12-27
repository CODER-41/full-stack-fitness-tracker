"""
Main application factory that initializes the Flask app and registers all components.
This file creates and configures the Flask Application with all neccessary extensions.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import Config

#Initialize extensions globally (but don't bind to app yet)
db = SQLAlchemy() #Database ORM for managing models
bcrypt = Bcrypt() #Password hashing for security
jwt = JWTManager() #JWT token authentication

def create_app():
    """Returns a configured Flask Application instance"""
    app = Flask(__name__)
    app.config.from_object(Config) #Load configuration from Config Class


    #Initialize extensions with the app (binds them to Flask Instance)
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    CORS(app) #Enable CrossOrigin Resource Sharing for frontend requests


    #Register blueprints  (route modules) with URL prefixes
    from routes.auth import auth_bp
    from routes.exercises import exercises_bp
    from routes.workouts import workouts_bp
    from routes.templates import templates_bp
    from routes.stats import stats_bp


    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(exercises_bp, url_prefix='/api/exercises')
    app.register_blueprint(workouts_bp, url_prefix='/api/workouts')
    app.register_blueprint(templates_bp, url_prefix='/api/templates')
    app.register_blueprint(stats_bp, url_prefix='/api/stats')

    return app

if __name__ == '__main__':
    #app instance
    app = create_app()


    #Database tables and seed default exercise on first run
    with app.app_context():
        db.create_all() #creates all tables defined in models

        from utils.seed_data import seed_default_exercises
        seed_default_exercises() #Populates default exercises if not already present

    
    #start development server
    app.run(debug=True, port=5000)


