"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    app.app_context().push()
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    """"create instances of Pet"""

    __tablename__ = "cupcakes"

    id = db.Column(
        db.Integer,
        autoincrement=True,
        primary_key=True
    )

    flavor = db.Column(
        db.String(50),
        nullable=False
    )

    size = db.Column(
        db.String(15),
        nullable=False
    )

    rating = db.Column(
        db.Integer,
        nullable=False

    )

    image_url = db.Column(
        db.Text(500),
        nullable=False,
        default="https://tinyurl.com/demo-cupcake"
    )