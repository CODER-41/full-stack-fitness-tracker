"""
Exercise model - represents individual exercises (like "Bench Press"  or "Squat")
Can be default exercises (available to all users ) or custom exercises (user-specific)
"""
from app import db
from datetime import datetime

class Exercise(db.Model):
    """
    Exercise table - library of all available exercises.
    Contains both default exercises (seeded) and user -created custom exercises.
    """

    #Primary key
    id = db.Column(db.Integer, primary_key=True)

    #Exercise details
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    muscle_group = db.Column(db.String(50))
    equipment = db.Column(db.String(50))


    # Flag to distinguish default vs custom exercises
    is_custom = db.Column(db.Boolean, default=False)  # False = default, True = custom
    

    # If custom exercise, links to the user who created it (nullable for default exercises)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    
    # Timestamp
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship back to user (only for custom exercises)
    creator = db.relationship('User', back_populates='custom_exercises')
