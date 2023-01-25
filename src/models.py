from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cities(db.Model):
    id = db.Column(db.String(300), primary_key=True)
    name = db.Column(db.String(300),nullable=True)
    ascii = db.Column(db.String(300),nullable=True)
    alt_name = db.Column(db.Text, nullable=True)
    lat = db.Column(db.String(300),nullable=True)
    long = db.Column(db.String(300),nullable=True)
    feat_class = db.Column(db.String(300),nullable=True)
    feat_code = db.Column(db.String(300),nullable = True)
    country = db.Column(db.String(300),nullable=True)
    cc2 = db.Column(db.String(300),nullable=True)
    admin1 = db.Column(db.String(300),nullable=True)
    admin2 = db.Column(db.String(300),nullable=True)
    admin3 = db.Column(db.String(300),nullable=True)
    admin4 = db.Column(db.String(300),nullable=True)
    population = db.Column(db.String(300),nullable=True)
    elevation = db.Column(db.String(300),nullable=True)
    dem = db.Column(db.String(300),nullable=True)
    tz = db.Column(db.String(300),nullable=True)
    modified_at = db.Column(db.String(300),nullable=True)

    def __repr__(self) -> str:
        return super().__repr__()