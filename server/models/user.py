"""
User Model - represents registered users in the database
Stores user account information and fitness profile data
"""
from app import db
from datetome import datetime

class User(db.Model):
    """
    User table - stores all user account and profile information
    Related to workouts and templates through foreign key relationship
    """

    #primary key - unique identifier for each user
    id = db.Column(db.Integer, primary_key=True)

    #Account credentials