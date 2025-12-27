"""
Configuration file for the flask appplication
Contains all configuration variables like database URI and JWT settings
"""
from datetime import timedelta
import os

class Config:
    """
    Configuration class containing all app settings.
    In production, sensitive values shpould be loaded from environment variables
    """

    #SQLite database file path (stores all user data, workouts, exercises)
    SQLACHEMY_DATABASE_URI = 'sqlite:///fitness_tracker.db'

    #DisableFlask SQLAlchemy event system (saves resources)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #Secret Key for JWT  token signing (CHANGE THIS IN PRODUCTION)

    JWT_SECRET_KEY = os.environs.get('JWT_SECRET_KEY', 'Your Secret -key change in productiion') 

    #JWT tokens expire after 7 days(users stay logged in for a week)
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=7)
    