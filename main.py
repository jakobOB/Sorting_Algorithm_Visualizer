import time
import pygame
from game import Game


def game_loop(game):
    while game.is_running:
        game.check_event()
        game.draw()
        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    game = Game()
    screen = pygame.display.set_mode((game.WIDTH, game.HEIGHT))
    game.screen = screen
    pygame.display.set_caption("SORTING VISUALISER")
    game.screen.fill(game.WHITE)
    game_loop(game)
    game.quit_game()
