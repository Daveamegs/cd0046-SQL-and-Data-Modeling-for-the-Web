from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False, unique=True)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), unique=True)
    genres = db.Column(db.ARRAY(db.String(50)), nullable=False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120), unique=True)
    seeking_talent = db.Column(
        db.Boolean, nullable=False, default=False)
    seeking_description = db.Column(db.Text)
    website_link = db.column(db.String(120))
    shows = db.relationship("Show", backref="shows",
                            cascade="all, delete", lazy=True)


class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120), unique=True)
    genres = db.Column(db.ARRAY(db.String(50)), nullable=False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120), unique=True)
    website_link = db.Column(db.String(120), nullable=True)
    seeking_venue = db.Column(
        db.Boolean, nullable=False, default=False)
    seeking_description = db.Column(db.Text)
    shows = db.relationship("Show", backref="show_list",
                            cascade="all, delete", lazy=True)


class Show(db.Model):
    __tablename__ = "shows"

    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey(
        "artist.id"), nullable=False)
    venue_id = db.Column(
        db.Integer, db.ForeignKey("venue.id"), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
