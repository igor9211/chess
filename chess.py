from abc import ABC, abstractmethod
import db


class Figure(ABC):
    def __init__(self, field: str, dest_field: str=None):
        self.field = field
        self.dest_field = dest_field

    @abstractmethod
    def list_available_moves(self, lista) -> list:
        movement_list: list = []
        field = db.Figure.query.filter_by(field=self.field).first()
        if field is None:
            return False
        position = [int(field.data[1]), int(field.data[4])]
        moves = lista(position)

        for i in moves:
            data = db.Figure.query.filter_by(data=str(i)).first()
            if data is not None:
                movement_list.append(data.field)
        return movement_list

    @abstractmethod
    def validate_move(self):
        pass


class King(Figure):
    def moves(self, position: list) -> list:
        lista: list = [
            [position[0] - 1, position[1] - 1],
            [position[0] - 1, position[1]],
            [position[0] - 1, position[1] + 1],
            [position[0], position[1] - 1],
            [position[0] + 1, position[1] - 1],
            [position[0] + 1, position[1]],
            [position[0] + 1, position[1] + 1],
            [position[0], position[1] + 1]
        ]
        return lista

    def list_available_moves(self) -> list:
        return Figure.list_available_moves(self, self.moves)

    def validate_move(self) -> bool:
        movement_list = King.list_available_moves(self)
        if self.dest_field in movement_list:
            return True
        else:
            return None


class Queen(Figure):
    def moves(self, a: list) -> list:
        lista: list = []
        for x in range(1, 8):
            move_up = [a[0] + x, a[1]]
            lista.append(move_up)

        for x in range(1, 8):
            move_down = [a[0] - x, a[1]]
            lista.append(move_down)

        for x in range(1, 8):
            move_right = [a[0], a[1] + x]
            lista.append(move_right)

        for x in range(1, 8):
            move_left = [a[0], a[1] - x]
            lista.append(move_left)

        for x in range(1, 8):
            move_left_up = [a[0] + x, a[1] - x]
            lista.append(move_left_up)

        for x in range(1, 8):
            move_right_up = [a[0] + x, a[1] + x]
            lista.append(move_right_up)

        for x in range(1, 8):
            move_left_down = [a[0] - x, a[1] - x]
            lista.append(move_left_down)

        for x in range(1, 8):
            move_right_down = [a[0] - x, a[1] + x]
            lista.append(move_right_down)
        return lista

    def list_available_moves(self) -> list:
        return Figure.list_available_moves(self, self.moves)

    def validate_move(self) -> bool:
        movement_list = Queen.list_available_moves(self)
        if self.dest_field in movement_list:
            return True
        else:
            return None


class Bishop(Figure):
    def moves(self, a: list) -> list:
        lista: list = []
        for x in range(1, 8):
            move_left_up = [a[0] + x, a[1] - x]
            lista.append(move_left_up)

        for x in range(1, 8):
            move_right_up = [a[0] + x, a[1] + x]
            lista.append(move_right_up)

        for x in range(1, 8):
            move_left_down = [a[0] - x, a[1] - x]
            lista.append(move_left_down)

        for x in range(1, 8):
            move_right_down = [a[0] - x, a[1] + x]
            lista.append(move_right_down)
        return lista

    def list_available_moves(self) -> list:
        return Figure.list_available_moves(self, self.moves)

    def validate_move(self) -> bool:
        movement_list = Bishop.list_available_moves(self)
        if self.dest_field in movement_list:
            return True
        else:
            return None


class Rook(Figure):
    def moves(self, a: list) -> list:
        lista: list = []
        for x in range(1, 8):
            move_up = [a[0] + x, a[1]]
            lista.append(move_up)

        for x in range(1, 8):
            move_down = [a[0] - x, a[1]]
            lista.append(move_down)

        for x in range(1, 8):
            move_right = [a[0], a[1] + x]
            lista.append(move_right)

        for x in range(1, 8):
            move_left = [a[0], a[1] - x]
            lista.append(move_left)
        return lista

    def list_available_moves(self) -> list:
        return Figure.list_available_moves(self, self.moves)

    def validate_move(self) -> bool:
        movement_list = Rook.list_available_moves(self)
        if self.dest_field in movement_list:
            return True
        else:
            return None


class Knight(Figure):
    def moves(self, a: list) -> list:
        lista: list = [
            [a[0] - 2, a[1] + 1],
            [a[0] - 1, a[1] + 2],
            [a[0] + 1, a[1] + 2],
            [a[0] + 2, a[1] + 1],
            [a[0] + 2, a[1] - 1],
            [a[0] + 1, a[1] - 2],
            [a[0] - 1, a[1] - 2],
            [a[0] - 2, a[1] - 1],
        ]
        return lista

    def list_available_moves(self) -> list:

        return Figure.list_available_moves(self, self.moves)

    def validate_move(self) -> bool:
        movement_list = Knight.list_available_moves(self)
        if self.dest_field in movement_list:
            return True
        else:
            return None


class Pawn(Figure):
    def moves(self, a: list) -> list:
        first_move = [[1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2]]
        if a in first_move:
            lista = [[a[0], a[1] + 1], [a[0], a[1] + 2]]
        else:
            lista = [[a[0], a[1] + 1]]

        return lista

    def list_available_moves(self) -> list:
        return Figure.list_available_moves(self, self.moves)

    def validate_move(self) -> bool:
        movement_list = Pawn.list_available_moves(self)
        if self.dest_field in movement_list:
            return True
        else:
            return None