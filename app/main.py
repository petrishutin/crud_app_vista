from logging import getLogger
from flask import Flask, render_template, request, redirect, url_for, session
from sqlalchemy import desc
from werkzeug.exceptions import BadRequest, InternalServerError

from models import Note
from models.db import Session
from config import SECRET_KEY


app = Flask(__name__)
app.config.update(SECRET_KEY=SECRET_KEY)

logger = getLogger(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    notes = Session.query(Note).order_by(desc('id')).all()
    return render_template('index.html', notes=notes)


@app.route('/new_note.html', methods=("GET", "POST",))
def create_note():
    if request.method == "GET":
        return render_template("new_note.html")
    form = request.form
    note_text = form['note_text']
    note = Note(note_text)
    Session.add(note)
    try:
        Session.commit()
    except Exception as e:
        logger.exception("Error creating note!")
        raise InternalServerError(f"Could not create new note! Error: {e}")
    return redirect(url_for("index"))


@app.route('/<note_id>/delete_note.html')
def delete_note(note_id):
    Session.query(Note).filter(Note.id == note_id).delete()
    try:
        Session.commit()
    except Exception as e:
        logger.exception("Error creating note!")
        raise InternalServerError(f"Could not delete note # {note_id}! Error: {e}")
    return redirect(url_for("index"))


@app.route('/<note_id>/update_note.html', methods=("GET", "POST",))
def update_note(note_id):
    note = Session.query(Note).filter(Note.id == note_id).first()
    if not note:
        logger.exception("Error updating note! Note dose not exist.")
        raise InternalServerError(f"Could not update. Note dose not exist!")
    if request.method == "GET":
        return render_template("update_note.html", note=note)
    form = request.form
    note.text = form['note_text']
    try:
        Session.commit()
    except Exception as e:
        logger.exception("Error updating note!")
        raise InternalServerError(f"Could not update note # {note_id}! Error: {e}")
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(port=8001, debug=True)