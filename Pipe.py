
# PIPE Class

import pygame
import random
import Constants


class Pipe:
    def __init__(self, win):
        self.lower_pipe = Constants.lower_pipe.convert_alpha()
        self.upper_pipe = Constants.upper_pipe.convert_alpha()

        self.pos_X = 350

        self.gap_height = 450
        self.pos_upper_Y = -200
        self.pos_lower_Y = self.pos_upper_Y + self.gap_height

        self.win = win

        self.pipe_timer = 0
        self.pipes = list()

        self.create_pipe()

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
        self.win.blit(self.upper_pipe, (self.pos_X, self.pos_upper_Y))
        self.win.blit(self.lower_pipe, (self.pos_X, self.pos_lower_Y))
