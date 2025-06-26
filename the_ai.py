import random
import copy

class AI:
    def __init__(self, level=1, player=2):
        self.level = level
        self.player = player

    def rnd(self, board):
        empty_square = board.get_empty_squares()
        if not empty_square:
            return None
        index = random.randrange(0, len(empty_square))
        
        return empty_square[index]
    
    def minimax(self, board, maximizing):
        #terminal case
        case = board.final_state()
        
        #if player 1 wins, (positive)
        if case == 1:
            return 1, None
    
        #if palyer 2 wins (negative)
        elif case == 2:
            return -1, None
        
        #if draw (zero)
        elif board.is_full():
            return 0, None
        
        if maximizing:
            max_eval = -100
            best_move = None
            empty_square = board.get_empty_squares()

            for (row, column) in empty_square:
                temp_board = copy.deepcopy(board)
                temp_board.mark_squares(row, column, self.player)
                eval = self.minimax(temp_board, False)[0]
                if eval > max_eval:
                    max_eval = eval
                    best_move = (row, column)

            return max_eval, best_move

        elif not maximizing:
            min_eval = 100
            best_move = None
            empty_square = board.get_empty_squares()

            for (row, column) in empty_square:
                temp_board = copy.deepcopy(board)
                temp_board.mark_squares(row, column, self.player)
                eval = self.minimax(temp_board, True)[0]
                if eval < min_eval:
                    min_eval = eval
                    best_move = (row, column)

            return min_eval, best_move

    def evaluation(self, main_board):
        if self.level == 0: #random choice
            eval = 'random'
            move = self.rnd(main_board)
        else: #minimax algorithm choice
            eval, move = self.minimax(main_board, False)

        print(f'AI has chosen to move in {move}, with an evaluation of: {eval}')
            
        return move