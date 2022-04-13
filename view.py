from chess import King, Queen, Bishop, Rook, Knight, Pawn
from flask_restful import Resource, abort


chess_figure: list = ["king", "queen", "bishop", "rook", "knight", "pawn"]


def list(figure: str, field: str) -> list:
    chess_dict: dict = {
        "king": King(field).list_available_moves(),
        "queen": Queen(field).list_available_moves(),
        "bishop": Bishop(field).list_available_moves(),
        "rook": Rook(field).list_available_moves(),
        "knight": Knight(field).list_available_moves(),
        "pawn": Pawn(field).list_available_moves(),
    }
    moves = chess_dict.get(figure.lower())
    return moves


def validate(figure: str, field: str, dest_field: str) -> bool:
    chess_dict: dict = {
        "king": King(field, dest_field).validate_move(),
        "queen": Queen(field, dest_field).validate_move(),
        "bishop": Bishop(field, dest_field).validate_move(),
        "rook": Rook(field, dest_field).validate_move(),
        "knight": Knight(field, dest_field).validate_move(),
        "pawn": Pawn(field, dest_field).validate_move(),
    }
    dest_field = chess_dict.get((figure.lower()))
    return dest_field


class List(Resource):
    def get(self, figure: str, field: str) -> dict:
        if figure.lower() not in chess_figure:
            abort(404, error="Chess figure doesn't exist")
        moves = list(figure, field)
        if moves is False:
            abort(409, availableMoves=[],
                  error="Field does not exist",
                  figure=figure.title(),
                  currentField=field.upper())
        return {"availableMoves": moves,
                "error": None,
                "figure": figure.title(),
                "currentField": field.upper()
                }


class Validate(Resource):
    def get(self, figure: str, field: str, dest_field: str) -> dict:
        error = None
        if figure.lower() not in chess_figure:
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
