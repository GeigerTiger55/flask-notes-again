"""Models for Notes app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

############################# Classes ##########################################

class Note(db.Model):
    """
    Creates a note instance.
    Class Methods:
    """

    __tablename__ = "notes"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
    )
    title = db.Column(
        db.Text,
        nullable=False,
    )
    created = db.Column(
        db.DateTime,
        nullable = False,
        default=db.func.now(),
    )
    content = db.Column(
        db.Text,
        nullable=False,
    )
    
    def serialize(self):
        """Serialize to dictionary"""
        
        return{
            "id": self.id,
            "title": self.title,
            "created": self.created,
            "content": self.content, 
        }