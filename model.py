import app


class Venue(app.db.Model):
    __tablename__ = 'venue'

    id = app.db.Column(app.db.Integer, primary_key=True)
    name = app.db.Column(app.db.String(), nullable=False, unique=True)
    city = app.db.Column(app.db.String(120), nullable=False)
    state = app.db.Column(app.db.String(120), nullable=False)
    address = app.db.Column(app.db.String(120), nullable=False)
    phone = app.db.Column(app.db.String(120), unique=True)
    genres = app.db.Column(app.db.ARRAY(app.db.String(50)), nullable=False)
    image_link = app.db.Column(app.db.String(500))
    facebook_link = app.db.Column(app.db.String(120), unique=True)
    seeking_talent = app.db.Column(
        app.db.Boolean, nullable=False, default=False)
    seeking_description = app.db.Column(app.db.Text)
    website_link = app.db.column(app.db.String(120))
    shows = app.db.relationship("Show", backref="shows",
                                cascade="all, delete", lazy=True)


class Artist(app.db.Model):
    __tablename__ = 'artist'

    id = app.db.Column(app.db.Integer, primary_key=True)
    name = app.db.Column(app.db.String, nullable=False, unique=True)
    city = app.db.Column(app.db.String(120))
    state = app.db.Column(app.db.String(120))
    phone = app.db.Column(app.db.String(120), unique=True)
    genres = app.db.Column(app.db.ARRAY(app.db.String(50)), nullable=False)
    image_link = app.db.Column(app.db.String(500))
    facebook_link = app.db.Column(app.db.String(120), unique=True)
    website_link = app.db.Column(app.db.String(120), nullable=True)
    seeking_venue = app.db.Column(
        app.db.Boolean, nullable=False, default=False)
    seeking_description = app.db.Column(app.db.Text)
    shows = app.db.relationship("Show", backref="show_list",
                                cascade="all, delete", lazy=True)


class Show(app.db.Model):
    __tablename__ = "shows"

    id = app.db.Column(app.db.Integer, primary_key=True)
    artist_id = app.db.Column(app.db.Integer, app.db.ForeignKey(
        "artist.id"), nullable=False)
    venue_id = app.db.Column(
        app.db.Integer, app.db.ForeignKey("venue.id"), nullable=False)
    start_time = app.db.Column(app.db.DateTime, nullable=False)
