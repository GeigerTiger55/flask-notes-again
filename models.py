"""Models for ... app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

############################# Classes ##########################################

######## The One in "One-Many"
class Note(db.Model):
    """
    Creates a note instance.
    Class Methods:
    """

    __tablename__ = "notes"
#     Requires a database be created in psql. Check terminal psql commands.

# Always check that Column is uppercase. Common bug. 
# Primary key auto sets nullable = False, & unique=True
    id = db.Column(
        db.Integer,
        unique=True,
        primary_key=True,
        autoincrement=True,
    )
    entry_date = db.Column(
        db.DateTime,
        nullable = False,
        default=db.func.now(),
    )
    note_text = db.Column(
        db.text,
        nullable=False,
    )