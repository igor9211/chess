from chess import King, Queen, Bishop, Rook, Knight, Pawn
from flask_restful import Resource, abort


chess_figure = ["king", "queen", "bishop", "rook", "knight", "pawn"]


def list(figure, field):
    chess_dict = {
        "king": King(field).list_available_moves(),
        "queen": Queen(field).list_available_moves(),
        "bishop": Bishop(field).list_available_moves(),
        "rook": Rook(field).list_available_moves(),
        "knight": Knight(field).list_available_moves(),
        "pawn": Pawn(field).list_available_moves(),
    }
    moves = chess_dict.get(str(figure).lower())
    return moves


def validate(figure, field, dest_field):
    chess_dict = {
        "king": King(field, dest_field).validate_move(),
        "queen": Queen(field, dest_field).validate_move(),
        "bishop": Bishop(field, dest_field).validate_move(),
        "rook": Rook(field, dest_field).validate_move(),
        "knight": Knight(field, dest_field).validate_move(),
        "pawn": Pawn(field, dest_field).validate_move(),
    }
    dest_field = chess_dict.get((str(figure).lower()))
    return dest_field


class List(Resource):
    def get(self, figure, field):
        if str(figure).lower() not in chess_figure:
            abort(404, error="Chess figure doesn't exist")
        moves = list(figure, field)
        if moves is False:
            abort(409, availableMoves=[],
                  error="Field does not exist",
                  figure=figure.title(),
                  currentField=str(field).upper())
        return {"availableMoves": moves,
                "error": None,
                "figure": figure.title(),
                "currentField": str(field).upper()
                }


class Validate(Resource):
    def get(self, figure, field, dest_field):
        error = None
        if str(figure).lower() not in chess_figure:
            abort(404, error="Chess figure doesn't exist")
        validation = validate(figure, field, dest_field)
        if validation is None:
            validation = "inwalid"
            error = "Current move is not permitted."
        else:
            validation = "valid"
        return {"move": validation,
                "figure": figure,
                "error": error,
                "currentField": field,
                "destField": dest_field
                }
