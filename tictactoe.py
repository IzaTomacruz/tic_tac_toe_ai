import sys
import pygame
import numpy as numpy
from constants import Constants

class FullGame(Constants):
    def __init__(self):
        super().__init__()
        pygame.init() 
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("TIC-TAC-TOE GAME")
        self.screen.fill(self.background)
        self.game = Game(self.screen)
        pygame.display.update()  

    def loop(self):
        board = self.game.board

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = event.pos
                    row = position[1] // self.square_size
                    column = position[0] // self.square_size

                    if board.empty_squares(row, column):
                        board.mark_squares(row, column, self.game.player)
                        self.game.next_turn()
                        self.game.draw_figure(row, column)
                        print(board.squares)

            pygame.display.update()

class Board(Constants):
    def __init__(self):
        super().__init__()
        self.squares = numpy.zeros((self.rows, self.columns))

    def mark_squares(self, row, column, player):
        self.squares[row][column] = player

    def empty_squares(self, row, column):
        return self.squares[row][column] == 0

class Game(Constants):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.board = Board()
        self.player = 1
        self.show_lines()

    def show_lines(self):
        #For vertical
        pygame.draw.line(self.screen, self.line_color, (self.square_size, 0),
                         (self.square_size, self.height), self.line_width)
        pygame.draw.line(self.screen, self.line_color, (self.width - self.square_size, 0),
                         (self.width - self.square_size, self.height), self.line_width)
        #For horizontal
        pygame.draw.line(self.screen, self.line_color, (0, self.square_size),
                         (self.width, self.square_size), self.line_width)
        pygame.draw.line(self.screen, self.line_color, (0, self.height - self.square_size),
                         (self.width, self.height - self.square_size), self.line_width)

    def draw_figure(self, row, column):
        if self.player == 1:
            #ascending
            start_asc = (column * self.square_size + self.offset,
                         row * self.square_size + self.square_size - self.offset)
            end_asc = (column * self.square_size + self.square_size - self.offset,
                       row * self.square_size + self.offset)
            pygame.draw.line(self.screen, self.cross_color, start_asc, end_asc, self.cross_width)

            #descending
            start_desc = (column * self.square_size + self.offset,
                          row * self.square_size + self.offset)
            end_desc = (column * self.square_size + self.square_size - self.offset,
                        row * self.square_size + self.square_size - self.offset)
            pygame.draw.line(self.screen, self.cross_color, start_desc, end_desc, self.cross_width)

        elif self.player == 2:
            center = (column * self.square_size + self.square_size // 2, row * self.square_size + self.square_size // 2)
            pygame.draw.circle(self.screen, self.circle_color, center, self.radius, self.circle_width)

    def next_turn(self):
        self.player = self.player % 2 + 1


