from chess import King, Queen, Bishop, Rook, Knight, Pawn


class TestKing:
    def test_moving(self):
        data = King(None).moving([1, 1])
        reply = ["b1", "b2", "a2"]
        assert data == reply

    def test_list_available_moves(self):
        data = King("a1").list_available_moves()
        reply = {
            "error": None,
            "figure": "King",
            "currentField": "a1",
            "availableMoves": ["b1", "b2", "a2"],
        }
        assert data == reply

        data_two = King("a15").list_available_moves()
        reply_two = (
            {"error": "Field does not exist.", "figure": "King", "currentField": "a15"},
            409,
        )
        assert data_two == reply_two

    def test_validate_move(self):
        data = King("a1", "b5").validate_move()
        reply = {
            "error": None,
            "figure": "King",
            "currentField": "a1",
            "move": "Not possible",
            "dest_field": "b5",
        }
        assert data == reply

        data_two = King("a1", "a2").validate_move()
        reply_two = {
            "error": None,
            "figure": "King",
            "currentField": "a1",
            "move": "valid",
            "dest_field": "a2",
        }
        assert data_two == reply_two


class TestQueen:
    def test_moving(self):
        data = Queen(None).moving([1, 1])
        reply = [
            "b1",
            "c1",
            "d1",
            "e1",
            "f1",
            "g1",
            "h1",
            "a2",
            "a3",
            "a4",
            "a5",
            "a6",
            "a7",
            "a8",
            "b2",
            "c3",
            "d4",
            "e5",
            "f6",
            "g7",
            "h8",
        ]
        assert data == reply

    def test_lists_available_moves(self):
        data = Queen("a1").list_available_moves()
        reply = {
            "error": None,
            "figure": "Queen",
            "currentField": "a1",
            "availableMoves": [
                "b1",
                "c1",
                "d1",
                "e1",
                "f1",
                "g1",
                "h1",
                "a2",
                "a3",
                "a4",
                "a5",
                "a6",
                "a7",
                "a8",
                "b2",
                "c3",
                "d4",
                "e5",
                "f6",
                "g7",
                "h8",
            ],
        }
        assert data == reply

        data_two = Queen("a15").list_available_moves()
        reply_two = (
            {
                "error": "Field does not exist.",
                "figure": "Queen",
                "currentField": "a15",
            },
            409,
        )
        assert data_two == reply_two

    def test_validate_move(self):
        data = Queen("a1", "a6").validate_move()
        reply = {
            "error": None,
            "figure": "Queen",
            "currentField": "a1",
            "move": "valid",
            "dest_field": "a6",
        }
        assert data == reply

        data_two = Queen("a1", "b5").validate_move()
        reply_two = {
            "error": None,
            "figure": "Queen",
            "currentField": "a1",
            "move": "Not possible",
            "dest_field": "b5",
        }
        assert data_two == reply_two


class TestBishop:
    def test_moving(self):
        data = Bishop(None).moving([1, 1])
        reply = ["b2", "c3", "d4", "e5", "f6", "g7", "h8"]
        assert data == reply

    def test_available_move(self):
        data = Bishop("a1").list_available_moves()
        reply = {
            "error": None,
            "figure": "Bishop",
            "currentField": "a1",
            "availableMoves": ["b2", "c3", "d4", "e5", "f6", "g7", "h8"],
        }
        assert data == reply

        data_two = Bishop("a15").list_available_moves()
        reply_two = (
            {
                "error": "Field does not exist.",
                "figure": "Bishop",
                "currentField": "a15",
            },
            409,
        )

        assert data_two == reply_two

    def test_validate_move(self):
        data = Bishop("a1", "a6").validate_move()
        reply = {
            "error": None,
            "figure": "Bishop",
            "currentField": "a1",
            "move": "Not possible",
            "dest_field": "a6",
        }
        assert data == reply

        data_two = Bishop("a1", "h8").validate_move()
        reply_two = {
            "error": None,
            "figure": "Bishop",
            "currentField": "a1",
            "move": "valid",
            "dest_field": "h8",
        }
        assert data_two == reply_two


class TestRook:
    def test_moving(self):
        data = Rook(None).moving([1, 5])
        reply = [
            "b5",
            "c5",
            "d5",
            "e5",
            "f5",
            "g5",
            "h5",
            "a6",
            "a7",
            "a8",
            "a4",
            "a3",
            "a2",
            "a1",
        ]
        assert data == reply

    def test_list_available_moves(self):
        data = Rook("a15").list_available_moves()
        reply = (
            {"error": "Field does not exist.", "figure": "Rook", "currentField": "a15"},
            409,
        )
        assert data == reply

        data_one = Rook("a5").list_available_moves()
        reply_one = {
            "error": None,
            "figure": "Rook",
            "currentField": "a5",
            "availableMoves": [
                "b5",
                "c5",
                "d5",
                "e5",
                "f5",
                "g5",
                "h5",
                "a6",
                "a7",
                "a8",
                "a4",
                "a3",
                "a2",
                "a1",
            ],
        }
        assert data_one == reply_one

    def test_valid_move(self):
        data = Rook("a1", "a3").validate_move()
        reply = {
            "error": None,
            "figure": "Rook",
            "currentField": "a1",
            "move": "valid",
            "dest_field": "a3",
        }
        assert data == reply

        data_two = Rook("a1", "c3").validate_move()
        reply_two = {
            "error": None,
            "figure": "Rook",
            "currentField": "a1",
            "move": "Not possible",
            "dest_field": "c3",
        }
        assert data_two == reply_two


class TestKnight:
    def test_moving(self):
        data = Knight(None).moving([3, 3])
        reply = ["a4", "b5", "d5", "e4", "e2", "d1", "b1", "a2"]
        assert data == reply

    def test_list_available_moves(self):
        data = Knight("a1").list_available_moves()
        reply = {
            "error": None,
            "figure": "Knight",
            "currentField": "a1",
            "availableMoves": ["b3", "c2"],
        }
        assert data == reply

        data_two = Knight("a15").list_available_moves()
        reply_two = (
            {
                "error": "Field does not exist.",
                "figure": "Knight",
                "currentField": "a15",
            },
            409,
        )
        assert data_two == reply_two

    def test_validate_move(self):
        data = Knight("a1", "a2").validate_move()
        reply = {
            "error": None,
            "figure": "Knight",
            "currentField": "a1",
            "move": "Not possible",
            "dest_field": "a2",
        }
        assert data == reply

        data_two = Knight("a1", "b3").validate_move()
        reply_two = {
            "error": None,
            "figure": "Knight",
            "currentField": "a1",
            "move": "valid",
            "dest_field": "b3",
        }
        assert data_two == reply_two


class TestPawn:
    def test_move(self):
        data = Pawn(None).moving([1, 1])
        error = {
            "error": "wrong position for Pawn",
            "figure": "Pawn",
            "currentField": None,
        }
        assert data == error

        data_two = Pawn(None).moving([2, 2])
        reply = ["b3", "b4"]
        assert data_two == reply

        data_two = Pawn(None).moving([3, 3])
        reply = ["c4"]
        assert data_two == reply

    def test_list_available_moves_1(self):

        one = Pawn("a1").list_available_moves()
        dict = {
            "error": "wrong position for Pawn",
            "figure": "Pawn",
            "currentField": "a1",
            "availableMoves": [],
        }
        assert one == dict

        two = Pawn("a2").list_available_moves()
        dict_2 = {
            "error": None,
            "figure": "Pawn",
            "currentField": "a2",
            "availableMoves": ["a3", "a4"],
        }
        assert two == dict_2

        three = Pawn("a15").list_available_moves()
        dict_3 = (
            {"error": "Field does not exist.", "figure": "Pawn", "currentField": "a15"},
            409,
        )
        assert three == dict_3

    def test_valid_move(self):

        one = Pawn("a2", "a3").validate_move()
        dict = {
            "error": None,
            "figure": "Pawn",
            "currentField": "a2",
            "move": "valid",
            "dest_field": "a3",
        }
        assert one == dict

        two = Pawn("a5", "b4").validate_move()
        dict_2 = {
            "error": None,
            "figure": "Pawn",
            "currentField": "a5",
            "move": "Not possible",
            "dest_field": "b4",
        }
        assert two == dict_2
