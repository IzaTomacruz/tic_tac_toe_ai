import sys
import pygame
from constants import Constants
from board import Board
from the_ai import AI

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
        ai = self.game.ai
        self.game.print_welcome()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:

                    #press g to change gamemode
                    if event.key == pygame.K_g:
                        self.game.change_game_mode()
                        print(f"changed to {self.game.game_mode}")

                    #press r to reset the game
                    elif event.key == pygame.K_r:
                        self.game.reset()
                        board = self.game.board
                        ai = self.game.ai
                        self.game.print_welcome()

                    #press 0 change level to random ai
                    elif event.key == pygame.K_0:
                        ai.level = 0
                        print("changed to level 0")

                    #press 1 change level to unbeatable ai
                    elif event.key == pygame.K_1:
                        ai.level = 1
                        print("changed to level 1")

                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = event.pos
                    row = position[1] // self.square_size
                    column = position[0] // self.square_size

                    if board.empty_squares(row, column) and self.game.running:
                        self.game.make_move(row, column)
                        winner = board.final_state()
                        if winner != 0:
                            print(f"Player {int(winner)} wins!")
                            self.game.running = False
                        elif board.is_full():
                            print("It's a draw!")
                            self.game.running = False

            if self.game.game_mode == 'ai' and self.game.player == ai.player and self.game.running:
                pygame.display.update()

                row, column = ai.evaluation(board)
                self.game.make_move(row, column)

                winner = board.final_state()
                if winner != 0:
                    print(f"Player {int(winner)} wins!")
                    self.game.running = False
                elif board.is_full():
                    print("It's a draw!")
                    self.game.running = False

            pygame.display.update()

class Game(Constants):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.ai = AI()
        self.board = Board()
        self.player = 1
        self.game_mode = 'ai'
        self.running = True
        self.show_lines()

    def make_move(self, row, column):
        self.board.mark_squares(row, column, self.player)  
        self.draw_figure(row, column)                     
        self.next_turn()            

    def show_lines(self):
        self.screen.fill(self.background)
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
            center = (column * self.square_size + self.square_size // 2,
                      row * self.square_size + self.square_size // 2)
            pygame.draw.circle(self.screen, self.circle_color, center, self.radius, self.circle_width)

    def next_turn(self):
        self.player = self.player % 2 + 1

    def change_game_mode(self):
        if self.game_mode == 'pvp':
            self.game_mode = 'ai'
        else:
            self.game_mode = 'pvp'

    def reset(self):
        self.__init__(self.screen)

    def is_over(self):
        return self.board.final_state() != 0 or self.board.is_full()
    
    def print_welcome(self):
        print("===================================")
        print("Welcome to TIC-TAC-TOE!")
        print("===================================")
        print("Game Modes:")
        print("PvP: Player vs Player")
        print("AI : Player vs Computer")
        print("-----------------------------------")
        print("Press G to toggle game mode")
        print("Press R to restart the game")
        print("Press 0 or 1 to change AI difficulty")
        print("   0 - Easy (Random)")
        print("   1 - Hard (Unbeatable)")
        print("-----------------------------------")
        if self.game_mode == 'ai':
            print("You are Player 1(X)")
            print("AI is Player 2(O)")
        else:
            print("Player 1(X) goes first.")
            print("Player 2(O) goes next.")
        print("===================================")



