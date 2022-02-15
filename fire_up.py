from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from chess import King, Queen, Bishop, Rook, Knight, Pawn

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///chess_sqlalchemy.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route("/king/<field>")
@app.route("/king/<field>/<dest_field>")
def king(field, dest_field=None):
    if dest_field is None:
        info = King(field).list_available_moves()
        return info
    else:
        info2 = King(field, dest_field).validate_move()
        return info2


@app.route("/queen/<field>")
@app.route("/queen/<field>/<dest_field>")
def queen(field, dest_field=None):
    if dest_field is None:
        info = Queen(field).list_available_moves()
        return info
    else:
        info2 = Queen(field, dest_field).validate_move()
        return info2


@app.route("/bishop/<field>")
@app.route("/bishop/<field>/<dest_field>")
def bishop(field, dest_field=None):
    if dest_field is None:
        info = Bishop(field).list_available_moves()
        return info
    else:
        info2 = Bishop(field, dest_field).validate_move()
        return info2


@app.route("/rook/<field>")
@app.route("/rook/<field>/<dest_field>")
def rook(field, dest_field=None):
    if dest_field is None:
        info = Rook(field).list_available_moves()
        return info
    else:
        info2 = Rook(field, dest_field).validate_move()
        return info2


@app.route("/knight/<field>")
@app.route("/knight/<field>/<dest_field>")
def knight(field, dest_field=None):
    if dest_field is None:
        info = Knight(field).list_available_moves()
        return info
    else:
        info2 = Knight(field, dest_field).validate_move()
        return info2


@app.route("/pawn/<field>")
@app.route("/pawn/<field>/<dest_field>")
def pawn(field, dest_field=None):
    if dest_field is None:
        info = Pawn(field).list_available_moves()
        return info
    else:
        info2 = Pawn(field, dest_field).validate_move()
        return info2


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

