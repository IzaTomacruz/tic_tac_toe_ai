import random

class AI:
    def __init__(self, level=0, player=2):
        self.level = level
        self.player = player

    def rnd(self, board):
        empty_square = board.get_empty_squares()
        index = random.randrange(0, len(empty_square))
        
        return empty_square[index]
    
    def evaluation(self, main_board):
        if self.level == 0: #random choice
            move = self.rnd(main_board)
        else: #minimax algorithm choice
            pass

        return move