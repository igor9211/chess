from src.chess import King, Queen, Bishop, Rook, Knight, Pawn, Figure
from unittest import TestCase


class ExampleFigure(Figure):
    def moves(self, a: list) -> list:
        moves: list = [[a[0], a[1] + 1]]
        return moves

    def list_available_moves(self) -> list:
        return Figure.list_available_moves(self, self.moves)

    def validate_move(self):
        pass


class TestFigure(TestCase):
    def test_list_available_moves(self):
        test: list = ExampleFigure("a5").list_available_moves()
        self.assertEqual(test, ['a6'])


class TestKing(TestCase):
    def test_moves(self):
        data: list = King(None).moves([1, 5])
        result: list = [[0, 4], [0, 5], [0, 6], [1, 4], [2, 4], [2, 5], [2, 6], [1, 6]]
        self.assertEqual(data, result)

    def test_list_available_moves(self):
        data: list = King("a5").list_available_moves()
        result: list = [
            "a4",
            "b4",
            "b5",
            "b6",
            "a6"
        ]
        self.assertEqual(data, result)

    def test_validation_move(self):
        data1: bool = King("a5", "a6").validate_move()
        data2: bool = King("a5", "c2").validate_move()
        self.assertTrue(data1)
        self.assertFalse(data2)


class TestQueen(TestCase):
    def test_moves(self):
        data: list = Queen(None).moves([1, 5])
        result: list = [[2, 5], [3, 5], [4, 5], [5, 5], [6, 5], [7, 5], [8, 5], [0, 5], [-1, 5], [-2, 5], [-3, 5], [-4, 5],
                  [-5, 5], [-6, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [1, 11], [1, 12], [1, 4], [1, 3], [1, 2],
                  [1, 1], [1, 0], [1, -1], [1, -2], [2, 4], [3, 3], [4, 2], [5, 1], [6, 0], [7, -1], [8, -2], [2, 6],
                  [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 12], [0, 4], [-1, 3], [-2, 2], [-3, 1], [-4, 0],
                  [-5, -1], [-6, -2], [0, 6], [-1, 7], [-2, 8], [-3, 9], [-4, 10], [-5, 11], [-6, 12]]
        self.assertEqual(data, result)

    def test_validation_move(self):
        data1: bool = Queen("a5", "a6").validate_move()
        data2: bool = Queen("a5", "c2").validate_move()
        self.assertTrue(data1)
        self.assertFalse(data2)


class TestBishop(TestCase):
    def test_moves(self):
        data: list = Bishop(None).moves([1, 5])
        result: list = [[2, 4], [3, 3], [4, 2], [5, 1], [6, 0], [7, -1], [8, -2], [2, 6], [3, 7], [4, 8], [5, 9],
                        [6, 10], [7, 11], [8, 12], [0, 4], [-1, 3], [-2, 2], [-3, 1], [-4, 0], [-5, -1], [-6, -2],
                        [0, 6], [-1, 7], [-2, 8], [-3, 9], [-4, 10], [-5, 11], [-6, 12]]
        self.assertEqual(data, result)

    def test_validation_move(self):
        data1: bool = Bishop("a5", "b4").validate_move()
        data2: bool = Bishop("a5", "c2").validate_move()
        self.assertTrue(data1)
        self.assertFalse(data2)


class TestRook(TestCase):
    def test_moves(self):
        date: list = Rook(None).moves([1, 5])
        result: list = [[2, 5], [3, 5], [4, 5], [5, 5], [6, 5], [7, 5], [8, 5], [0, 5], [-1, 5], [-2, 5], [-3, 5],
                        [-4, 5], [-5, 5], [-6, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [1, 11], [1, 12], [1, 4],
                        [1, 3], [1, 2], [1, 1], [1, 0], [1, -1], [1, -2]]
        self.assertEqual(date, result)

    def test_validatino_move(self):
        data1: bool = Rook("a5", "a6").validate_move()
        data2: bool = Rook("a5", "c2").validate_move()
        self.assertTrue(data1)
        self.assertFalse(data2)


class TestKnight(TestCase):
    def test_moves(self):
        data: list = Knight(None).moves([1,5])
        result: list = [[-1, 6], [0, 7], [2, 7], [3, 6], [3, 4], [2, 3], [0, 3], [-1, 4]]
        self.assertEqual(data, result)

    def test_validation_move(self):
        data1: bool = Knight("a5", "b7").validate_move()
        data2: bool = Knight("a5", "c2").validate_move()
        self.assertTrue(data1)
        self.assertFalse(data2)


class TestPawn(TestCase):
    def test_moves(self):
        data: list = Pawn(None).moves([1, 5])
        result: list = [[1, 6]]
        self.assertEqual(data, result)

    def test_validation_move(self):
        data1: bool = Pawn("a5", "a6").validate_move()
        data2: bool = Pawn("a6", "c2").validate_move()
        self.assertTrue(data1)
        self.assertFalse(data2)