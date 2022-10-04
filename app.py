"""Flask app for ..."""

from flask import Flask, jsonify, request, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Note
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# TODO: should these be included with sqlite??????*******
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "SECRETKEY"
app.config['SQLALCHEMY_ECHO'] = True

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)

connect_db(app)

# def get_db_connection():
#     conn = sqlite3.connect('database.db')
#     conn.row_factory = sqlite3.Row
#     return conn


@app.get('/api/notes')
def get_all_notes():
    """Return JSON list of notes
        - {'notes': [{id, title, created, content}, ...]}
    """
    
    
    notes = Note.query.all()
    # TODO: add serializers
    serialized = notes
    return jsonify(notes=serialized)

# Thinking space
# ----
# Use sqLite - done
# Create a table /w sqLite - done
# ----
# Routes
# Restful
# Get 1 note
# Get all notes
# Get note(s) by filter
# ----
# API Insomnia Post & Delete a note
