from unittest import TestCase
from src import view


class TestFun(TestCase):
    def test_list(self):
        figure: str = "king"
        field: str = "a7"
        data = view.list(figure, field)
        result: list = ['a6', 'b6', 'b7', 'b8', 'a8']
        self.assertEqual(data, result)

    def test_validate(self):
        figure: str = "king"
        field: str = "a7"
        dest_field: str = "a8"
        data = view.validate(figure, field, dest_field)
        self.assertTrue(data)


class TestList(TestCase):
    def test_get(self):
        figure: str = "king"
        field: str = "a2"
        data = view.List().get(figure, field)
        result: dict = {'availableMoves': ['a1', 'b1', 'b2', 'b3', 'a3'],
                        'error': None,
                        'figure': 'King',
                        'currentField': 'A2'
                        }
        self.assertEqual(data, result)


class TestValidate(TestCase):
    def test_get(self):
        figure: str = "king"
        field: str = "a2"
        dest_field: str = "a3"
        data = view.Validate().get(figure, field, dest_field)
        result: dict ={
            "move": "valid",
            "figure": "king",
            "error": None,
            "currentField": "a2",
            "destField": "a3"
        }



