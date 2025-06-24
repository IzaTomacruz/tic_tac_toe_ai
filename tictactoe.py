import sys
import pygame
import numpy as numpy
from constants import *

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("TIC-TAC-TOE GAME")
screen.fill(background)

class Board:
    def __init__(self):
        self.squares = numpy.zeros((rows, columms))

    def mark_squares(self, row, column, player):
        self.squares[row][column] = player

    def empty_squares(self, row, column):
        return self.squares[row][column] == 0

class Game:
    def __init__(self):
        self.board = Board()
        self.player = 1
        self.show_lines()

    def show_lines(self):
        #For vertical
        pygame.draw.line(screen, line_color, (square_size, 0), (square_size, height), line_width)
        pygame.draw.line(screen, line_color, (width - square_size, 0), (width - square_size, height), line_width)
        #For horizontal
        pygame.draw.line(screen, line_color, (0, square_size), (width, square_size), line_width)
        pygame.draw.line(screen, line_color, (0, height - square_size), (width, height - square_size), line_width)

    def next_turn(self):
        self.player = self.player % 2 + 1

def main():
    game = Game()
    board = game.board

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                position = event.pos
                row = position[1] // square_size
                column = position[0] // square_size
              
                
                if board.empty_squares(row, column):
                    board.mark_squares(row, column, game.player)
                    game.next_turn()
                    print(board.squares)

        pygame.display.update()

main()