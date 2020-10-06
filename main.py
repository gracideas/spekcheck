from datetime import datetime
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from forms import SubmissionForm
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

SECRET_KEY = 'hrifrgtkghgt'
UPLOAD_FOLDER = '/uploads' #temporary
ALLOWED_EXTENSIONS = {'cue', 'log','flac', 'mp3', 'opus', 'wav', 'm4a', 'ogg', 'acc'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = SECRET_KEY
db_name = 'site.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


# Database tables
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, index=True, nullable=False)
    entry_count = db.Column(db.Integer, unique=False, nullable=False, default=0)
    moderator = db.Column (db.Boolean, unique=False, nullable=False, default=False)
    user_id = db.relationship('User', backref='author', lazy=True)

    def __repr__(self):
        return f"Metadata({self.release_title}, {self.release_artist})"


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    musicbrainz_album_id = db.Column(db.String(36), index=True, nullable=False)
    audio_format = db.Column(db.String, nullable=False)
    notes = db.Column(db.String, unique=False, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    entry_id = db.Column(db.Integer, db.ForeignKey('entry.id'))


    def __repr__(self):
        return f"Entry({self.musicbrainz_album_id}, {self.date_created})"

class Metadata(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    catalog_number = db.Column(db.String, nullable=False)
    release_artist = db.Column(db.String, nullable=False)
    release_name = db.Column(db.String, nullable=False)
    physical_format = db.Column(db.String, nullable=False)
    entry_id = db.Column(db.Integer, db.ForeignKey('entry.id'))

    def __repr__(self):
        return f"Metadata({self.release_title}, {self.release_artist})"


# Dummy Entry to test templating
posts = [
    {
        'release': 'Myst3ry',
        'artist': 'Ladies Code',
        'catalog': 'L200001886',
        'physicalformat': 'CD',
        'audioformat': 'FLAC',
        'notes': 'The spectograph of this release cuts off abruptly at 20db. This is likely due to how the song was produced or mastered.'

    }
]

# Renders routes from templates
@app.route("/")
def home():
    return render_template("search.html", title='Search')

@app.route("/search")
def search():
    return render_template("search.html", title='Search')


@app.route("/leaderboard")
def leaderboard():
    return render_template("leaderboard.html", title='Leaderboard')


@app.route("/entry")
def entry():
    return render_template("entry.html", posts=posts)


@app.route("/login")
def login():
    return render_template("login.html", title='Login')


@app.route("/logout")
def logout():
    return redirect(url_for('/'))  # Returns to home page after logout

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

@app.route("/submit", methods=['GET', 'POST'])
def submit():
    form= SubmissionForm()
    if form.validate_on_submit():
        # Defines new variables from the form fields
        musicbrainz_album_id = request.form['musicbrainz_album_id']
        source = request.form['source']

        entry = (musicbrainz_album_id, source)
        print(str(entry))

        # Commits entry to database
        db.session.add(entry)
        db.session.commit()
        
        flash(f'Submitted your files!')

        return redirect(url_for('home'))
    else: 
        print('error')
    return render_template("submit.html", title='Submit', form=form)
    
if __name__ == "__main__":  # Lets you see the changes live 
    app.run(debug=True)


