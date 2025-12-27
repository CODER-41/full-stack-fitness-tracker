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

    #Account credentials(must be unique)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), unique =True, nullable=False) #Stored as bcrypt hash

    
    #User profile information (optional)
    age = db.Column(db.Integer)
    weight = db.Column(db.Float)
    height = db.Column(db.Float)
    fitness_goal = db.Column(db.String(200))

    #Timestamp for when account was created 
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    #Relationship to other tables
    #Cascade = 'all, delete-orphan' means deleting a user also deletes their workouts/Templates
    workouts = db.relationship('Workout', back_populates='user', lazy=True, cascade='all, delete-orphan')
    templates = db.relationship('WorkoutTemplate', back_populates='user', lazy=True, cascade='all, delete-orphan')
    custom_exercises = db.relationship('Exercise', back_populates='creator', lazy=True, cascade='all, delete-orphan')