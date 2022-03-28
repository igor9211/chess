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