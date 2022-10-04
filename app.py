"""Flask app for ..."""

from flask import Flask, jsonify, request, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Note
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "SECRETKEY"
app.config['SQLALCHEMY_ECHO'] = True

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)

connect_db(app)

@app.get('/api/notes')
def get_all_notes():
    """Return JSON list of notes
        - {'notes': [{id, title, created, content}, ...]}
    """
    
    notes = Note.query.all()
    serialized = [n.serialize() for n in notes]
    return jsonify(notes=serialized)

@app.get('/api/notes/<int:n_id>')
def get_single_note(n_id):
    """Return JSON with info about single note
        - {'note': {id, title, created, content}}
    """
    
    note = Note.query.get_or_404(n_id)
    serialized = note.serialize()
    return jsonify(note=serialized)
    
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
