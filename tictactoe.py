import sys
import pygame
from constants import *

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("TIC-TAC-TOE GAME")
screen.fill(background)

class Game:
    def __init__(self):
        self.show_lines()

    def show_lines(self):
        #For vertical
        pygame.draw.line(screen, line_color, (square_size, 0), (square_size, height), line_width)
        pygame.draw.line(screen, line_color, (width - square_size, 0), (width - square_size, height), line_width)
        #For horizontal
        pygame.draw.line(screen, line_color, (0, square_size), (width, square_size), line_width)
        pygame.draw.line(screen, line_color, (0, height - square_size), (width, height - square_size), line_width)

def main():
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

main()