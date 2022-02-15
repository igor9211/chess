from abc import ABC, abstractmethod
import requests
import insert


class Figure(ABC):
    def __init__(self, field, dest_field=None):
        self.field = field
        self.dest_field = dest_field
        self.movement_list = []
        self.error = None
        self.dict = {
            "error": self.error,
            "figure": None,
            "currentField": None,
        }
        self.position = []
        self.request = requests.get("http://httpbin.org/status/409")

    @abstractmethod
    def list_available_moves(self):
        data = insert.Create.query.filter_by(field=self.field).first()
        if data is None:
            self.error = "Field does not exist."
            self.dict["currentField"] = self.field
            self.dict["error"] = self.error
            return self.dict
        self.position = [int(data.data[1]), int(data.data[4])]
        return self.position

    @abstractmethod
    def validate_move(self):
        self.dict.pop("availableMoves")
        if self.dest_field in self.movement_list:
            move = "valid"
            self.dict["move"] = move
            self.dict["dest_field"] = self.dest_field
        else:
            move = "Not possible"
            self.dict["move"] = move
            self.dict["dest_field"] = self.dest_field
        return self.dict


class King(Figure):
    def moving(self, a):
        lista = [
            [a[0] - 1, a[1] - 1],
            [a[0] - 1, a[1]],
            [a[0] - 1, a[1] + 1],
            [a[0], a[1] - 1],
            [a[0] + 1, a[1] - 1],
            [a[0] + 1, a[1]],
            [a[0] + 1, a[1] + 1],
            [a[0], a[1] + 1],
        ]
        self.movement_list = []
        for i in lista:
            data = insert.Create.query.filter_by(data=str(i)).first()
            if data is not None:
                self.movement_list.append(data.field)
        return self.movement_list

    def list_available_moves(self):
        Figure.list_available_moves(self)
        if not self.position:
            self.dict["figure"] = "King"
            return self.dict, self.request.status_code
        King.moving(self, self.position)
        self.dict["figure"] = "King"
        self.dict["availableMoves"] = self.movement_list
        self.dict["currentField"] = self.field
        return self.dict

    def validate_move(self):
        King.list_available_moves(self)
        return Figure.validate_move(self)


class Queen(Figure):
    def moving(self, a):
        lista = []
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

        self.movement_list = []
        for i in lista:
            data = insert.Create.query.filter_by(data=str(i)).first()
            if data is not None:
                self.movement_list.append(data.field)
        return self.movement_list

    def list_available_moves(self):
        Figure.list_available_moves(self)
        if not self.position:
            self.dict["figure"] = "Queen"
            return self.dict, self.request.status_code
        Queen.moving(self, self.position)
        self.dict["figure"] = "Queen"
        self.dict["availableMoves"] = self.movement_list
        self.dict["currentField"] = self.field
        return self.dict

    def validate_move(self):
        Queen.list_available_moves(self)
        return Figure.validate_move(self)


class Bishop(Figure):
    def moving(self, a):
        lista = []
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

        self.movement_list = []
        for i in lista:
            data = insert.Create.query.filter_by(data=str(i)).first()
            if data is not None:
                self.movement_list.append(data.field)
        return self.movement_list

    def list_available_moves(self):
        Figure.list_available_moves(self)
        if not self.position:
            self.dict["figure"] = "Bishop"
            return self.dict, self.request.status_code
        Bishop.moving(self, self.position)
        self.dict["figure"] = "Bishop"
        self.dict["availableMoves"] = self.movement_list
        self.dict["currentField"] = self.field
        return self.dict

    def validate_move(self):
        Bishop.list_available_moves(self)
        return Figure.validate_move(self)


class Rook(Figure):
    def moving(self, a):
        lista = []
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

        self.movement_list = []
        for i in lista:
            data = insert.Create.query.filter_by(data=str(i)).first()
            if data is not None:
                self.movement_list.append(data.field)
        return self.movement_list

    def list_available_moves(self):
        Figure.list_available_moves(self)
        if not self.position:
            self.dict["figure"] = "Rook"
            return self.dict, self.request.status_code
        Rook.moving(self, self.position)
        self.dict["figure"] = "Rook"
        self.dict["availableMoves"] = self.movement_list
        self.dict["currentField"] = self.field
        return self.dict

    def validate_move(self):
        Rook.list_available_moves(self)
        return Figure.validate_move(self)


class Knight(Figure):
    def moving(self, a):
        lista = [
            [a[0] - 2, a[1] + 1],
            [a[0] - 1, a[1] + 2],
            [a[0] + 1, a[1] + 2],
            [a[0] + 2, a[1] + 1],
            [a[0] + 2, a[1] - 1],
            [a[0] + 1, a[1] - 2],
            [a[0] - 1, a[1] - 2],
            [a[0] - 2, a[1] - 1],
        ]
        self.movement_list = []
        for i in lista:
            data = insert.Create.query.filter_by(data=str(i)).first()
            if data is not None:
                self.movement_list.append(data.field)
        return self.movement_list

    def list_available_moves(self):
        Figure.list_available_moves(self)
        if not self.position:
            self.dict["figure"] = "Knight"
            return self.dict, self.request.status_code
        Knight.moving(self, self.position)
        self.dict["figure"] = "Knight"
        self.dict["availableMoves"] = self.movement_list
        self.dict["currentField"] = self.field
        return self.dict

    def validate_move(self):
        Knight.list_available_moves(self)
        return Figure.validate_move(self)


class Pawn(Figure):
    def moving(self, a):
        wrong_position = [
            [1, 1],
            [2, 1],
            [3, 1],
            [4, 1],
            [5, 1],
            [6, 1],
            [7, 1],
            [8, 1],
        ]
        first_move = [[1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2]]
        if a in wrong_position:
            self.error = "wrong position for Pawn"
            self.dict["figure"] = "Pawn"
            self.dict["error"] = self.error
            return self.dict
        if a in first_move:
            lista = [[a[0], a[1] + 1], [a[0], a[1] + 2]]
        else:
            lista = [[a[0], a[1] + 1]]
        self.movement_list.clear()
        for i in lista:
            data = insert.Create.query.filter_by(data=str(i)).first()
            if data is not None:
                self.movement_list.append(data.field)
        return self.movement_list

    def list_available_moves(self):
        Figure.list_available_moves(self)
        if not self.position:
            self.dict["figure"] = "Pawn"
            return self.dict, self.request.status_code
        Pawn.moving(self, self.position)
        self.dict["figure"] = "Pawn"
        self.dict["availableMoves"] = self.movement_list
        self.dict["currentField"] = self.field
        return self.dict

    def validate_move(self):
        Pawn.list_available_moves(self)
        return Figure.validate_move(self)


