import pygame
import random
from algorithms.merge_sort import *
from algorithms.bubble_sort import *


class Bar:
    def __init__(self, value=None, color=None):
        self.value = value
        self.color = color   # White = unsorted, Green = sorted, Red = on look


class Visualizer:
    def __init__(self):
        self.is_running = True
        self.is_sorting = False
        self.screen = None
        self.WIDTH = 900
        self.HEIGHT = 600
        self.WHITE, self.BLACK = (255, 255, 255), (0, 0, 0, 100)
        self.GREEN, self.LIGHT_GREEN = (0, 200, 0), (0, 255, 0)
        self.RED, self.LIGHT_RED = (200, 0, 0), (255, 0, 0)
        self.ORANGE = (255, 102, 0)
        self.font = pygame.font.SysFont("comicsans", 30)
        self.ARRAY_SIZE = 100
        self.array = [Bar(i, self.GREEN) for i in range(1, self.ARRAY_SIZE + 1)]  # [[value, color]]
        self.algorithms = {"Merge Sort": [merge_sort, (self, 0, len(self.array)-1)],
                           "Bubble Sort": [bubble_sort, (self, None)]}
        self.algorithm = "Choose Algorithm"

    def shuffle_array(self):
        random.shuffle(self.array)
        for arr in self.array:
            arr.color = self.GREEN
        self.refill()

    def __text_objects(self, text, font):
        text_surf = font.render(text, True, self.BLACK)
        return text_surf, text_surf.get_rect()

    def __animation(self):
        self.shuffle_array()
        # for i in range(6):
        #     for arr in self.array:
        #         arr.color = self.RED if i%2==0 else self.GREEN
        self.refill()
        #     time.sleep(1/3)

    def __draw_button(self, msg, x, y, width, height, color_a, color_i, action=None, args=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed(3)

        if x < mouse[0] < x + width and y < mouse[1] < y + height:
            pygame.draw.rect(self.screen, color_a, (x, y, width, height))
            if click[0] and action and not self.is_sorting:
                self.algorithm = msg
                self.is_sorting = True
                self.__animation()
                action(*args)
                for arr in self.array:
                    arr.color = self.ORANGE
                    self.refill()
                self.is_sorting = False
                self.algorithm = "Choose Algorithm"
        else:
            pygame.draw.rect(self.screen, color_i, (x, y, width, height))

        text_surf, text_rect = self.__text_objects(msg, self.font)
        text_rect.center = (x + (width / 2), y + (height / 2))
        self.screen.blit(text_surf, text_rect)

    def __draw_bars(self, left, top, width, height):
        rect = [left - 5, top, width + 5, height + 5]
        bar_width = width / len(self.array)
        bar_offset = bar_width / 10  # 10% from width

        shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
        pygame.draw.rect(shape_surf, self.BLACK, shape_surf.get_rect())
        self.screen.blit(shape_surf, rect)

        for idx, bar in enumerate(self.array):
            y = left + (idx * bar_width)
            x = (height * bar.value) / self.ARRAY_SIZE
            pygame.draw.line(self.screen, bar.color, (y, top), (y, x), int(bar_width - bar_offset))

    def __draw_label(self, x, msg="Choose Algorithm"):
        text_surf, text_rect = self.__text_objects(msg, self.font)
        text_rect.center = (self.WIDTH / 2, x)
        self.screen.blit(text_surf, text_rect)

    def refill(self, delay=20):
        self.screen.fill(self.WHITE)
        self.draw()
        pygame.display.update()
        pygame.time.delay(delay)

    def draw(self):
        self.check_event()
        self.screen.fill(self.WHITE)
        left = self.WIDTH / 10
        top = 0
        width = self.WIDTH - (self.WIDTH / 5)
        height = self.HEIGHT - (self.HEIGHT / 5)
        btn_height = (self.HEIGHT - height) / 2

        self.__draw_bars(left, top, width, height)
        self.__draw_label(height+30, self.algorithm)

        for idx, algo in enumerate(self.algorithms):
            offset = 10 + (160*idx)
            self.__draw_button(algo, offset, height + btn_height, 150, 50, self.LIGHT_GREEN, self.GREEN,
                               self.algorithms[algo][0], args=self.algorithms[algo][1])

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_visualizer()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit_visualizer()

    def quit_visualizer(self):
        pygame.quit()
        quit()
