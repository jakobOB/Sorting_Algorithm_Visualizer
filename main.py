import pygame
from visualizer import Visualizer


def game_loop(visualizer):
    while visualizer.is_running:
        visualizer.check_event()
        visualizer.draw()
        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    visualizer = Visualizer()
    screen = pygame.display.set_mode((visualizer.WIDTH, visualizer.HEIGHT))
    visualizer.screen = screen
    pygame.display.set_caption("SORTING VISUALISER")
    visualizer.screen.fill(visualizer.WHITE)
    game_loop(visualizer)
    visualizer.quit_game()
