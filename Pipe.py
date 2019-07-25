
# PIPE Class

import pygame
import random
import Constants


class Pipe:
    def __init__(self, win, lower_pipe, upper_pipe):
        self.lower_pipe = lower_pipe
        self.upper_pipe = upper_pipe

        self.pos_X = 350

        self.gap_height = 450
        self.pos_upper_Y = -200
        self.pos_lower_Y = self.pos_upper_Y + self.gap_height

        self.win = win

        self.pipe_timer = 0
        self.pipes = list()

        self.create_pipe()

    def is_collision(self, bird):
        lower_rect = pygame.Rect(self.pos_X, self. pos_lower_Y, 52, 320)
        upper_rect = pygame.Rect(self.pos_X, self. pos_upper_Y, 52, 320)

        if lower_rect.colliderect(bird.flap_rect):
            print("is collided")
            return True

        if upper_rect.colliderect(bird.flap_rect):
            print("is collided")
            return True

    @staticmethod
    def get_random_number():
        number = random.randint(1, 11)
        return number

    def calculate_position(self, random_number):
        self.pos_upper_Y = random_number * 20 - 300
        self.pos_lower_Y = self.pos_upper_Y + self.gap_height

    def create_pipe(self):
        random_number = self.get_random_number()
        self.calculate_position(random_number)

    def update_pipe(self):
        self.pos_X -= Constants.SPEED

    def draw_pipe(self):
        pygame.draw.rect(self.win, (0, 0, 255), (self.pos_X, self.pos_lower_Y, 52, 320))
        pygame.draw.rect(self.win, (0, 0, 255), (self.pos_X, self.pos_upper_Y, 52, 320))

        self.win.blit(self.upper_pipe, (self.pos_X, self.pos_upper_Y))
        self.win.blit(self.lower_pipe, (self.pos_X, self.pos_lower_Y))
