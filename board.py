import numpy as numpy
from constants import Constants

class Board(Constants):
    def __init__(self):
        super().__init__()
        self.squares = numpy.zeros((self.rows, self.columns))
        self.empty_square = self.squares
        self.marked_squares = 0

    def final_state(self):
        for column in range(self.columns):
            if self.squares[0][column] == self.squares[1][column] == self.squares[2][column] != 0:
                return self.squares[0][column]

        for row in range(self.rows):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                return self.squares[row][0]

        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            return self.squares[1][1]
        
        if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != 0:
            return self.squares[1][1]
        
        return 0 #means no win yet
        
    def mark_squares(self, row, column, player):
        self.squares[row][column] = player
        self.marked_squares += 1

    def empty_squares(self, row, column):
        return self.squares[row][column] == 0
    
    def get_empty_squares(self):
        empty_square = []
        for row in range(self.rows):
            for column in range(self.columns):
                if self.empty_square(row, column):
                    empty_square.append((row, column))

        return empty_square
    
    def is_full(self):
        return self.marked_squares == 9
    
    def is_empty(self):
        return self.mark_squares == 0