import chess_engine


def main():
    game_state = chess_engine.game_state()

    # מהלך 1: לבן - פיון מ-(1,3) ל-(3,3)
    game_state.white_turn = True
    start = (1, 3)
    end = (3, 3)
    game_state.move_piece(start, end, is_ai=False)
    piece = game_state.get_piece(*end).get_name()

    # מהלך 2: שחור - פיון מ-(6,3) ל-(4,3)
    game_state.white_turn = False
    start = (6, 3)
    end = (4, 3)
    game_state.move_piece(start, end, is_ai=False)
    piece = game_state.get_piece(*end).get_name()

    # מהלך 3: לבן - מלכה מ-(0,4) ל-(2,2)
    game_state.white_turn = True
    start = (0, 4)
    end = (2, 2)
    game_state.move_piece(start, end, is_ai=False)
    piece = game_state.get_piece(*end).get_name()

    # מהלך 4: שחור - פרש מ-(7,1) ל-(5,0)
    game_state.white_turn = False
    start = (7, 1)
    end = (5, 0)
    game_state.move_piece(start, end, is_ai=False)
    piece = game_state.get_piece(*end).get_name()

    # מהלך 5: לבן - רץ מ-(0,2) ל-(3,5)
    game_state.white_turn = True
    start = (0, 2)
    end = (3, 5)
    game_state.move_piece(start, end, is_ai=False)
    piece = game_state.get_piece(*end).get_name()

    # מהלך 6: שחור - פרש מ-(5,0) ל-(3,1)
    game_state.white_turn = False
    start = (5, 0)
    end = (3, 1)
    game_state.move_piece(start, end, is_ai=False)
    piece = game_state.get_piece(*end).get_name()

    # מהלך 7: לבן - מלכה מ-(2,2) ל-(6,2) — מט
    game_state.white_turn = True
    start = (2, 2)
    end = (6, 2)
    game_state.move_piece(start, end, is_ai=False)
    piece = game_state.get_piece(*end).get_name()
# בדיקת סוף המשחק
    game_state.checkmate_stalemate_checker()


if __name__ == "__main__":
    main()
