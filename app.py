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
    """Return JSON list of all notes
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

@app.get('/api/notes/<n_value>')
def get_filtered_notes(n_value):
    """Return JSON with info about all notes whose title contains the query
    parameter value.
        - {'notes': [{id, title, created, content}, ...]}
    """

    notes = Note.query.filter(Note.title.like(f'%{n_value}%'))
    serialized = [n.serialize() for n in notes]
    return jsonify(notes=serialized)

# Post a Note route
@app.post('/api/notes')
def create_note():
    """Create a new note instance in databse.
    Return JSON with info about the created note.
    Only creates 1 note at a time."""

    new_note = Note(
        title = request.json["title"],
        content = request.json["content"],
    )

    db.session.add(new_note)
    db.session.commit()

    serialized = new_note.serialize()
    return (jsonify(note=serialized),201)


# Thinking space
# ----
# Use sqLite - done
# Create a table /w sqLite - done
# ----
# Restful Routes
# Get 1 note - done
# Get all notes - done
# Get note(s) by filter - done
# ----
# API Insomnia Post & Delete a note
