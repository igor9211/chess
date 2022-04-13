import string
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///chess_sqlalchemy.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Figure(db.Model):

    __tablename__ = "figure"

    field = db.Column(db.String, primary_key=True)
    data = db.Column(db.String)

    def __init__(self, field, data):
        self.field = field
        self.data = data


def preparation_data(*args):
    for x in range(1, 9):
        field = str(args[0]) + str(x)
        data = [int(args[1]), x]
        next_field = Figure(str(field), str(data))
        db.session.add(next_field)


def insert():
    a_to_h = string.ascii_lowercase[:8]
    numbers = range(1, 9)
    for y in range(0, 8):
        preparation_data(a_to_h[y], numbers[y])


# db.create_all()
# insert()
# db.session.commit()
