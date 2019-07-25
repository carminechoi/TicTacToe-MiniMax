

# Carmine Choi
# July 16, 2019

import os
import pygame
import Pipe
import Bird
import Constants

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (600, 200)


class Game:

    def __init__(self):

        global win
        win = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))

        self.ground1_posx = -168
        self.ground2_posx = 168
        self.ground_posy = 400

        self.bird = list()
        self.bird.append(Bird.Bird(win))

        self.pipe_timer = 0

        self.game_over = False
        self.pipes = list()
        self.pipes.append(Pipe.Pipe(win))

        self.clock = pygame.time.Clock()

    def game_loop(self):
        while not self.game_over:
            for event in pygame.event.get():
                # if exit is pressed
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # MOVE GROUND
            if self.ground1_posx <= -335:
                self.ground1_posx = -168
            else:
                self.ground1_posx -= Constants.SPEED
            if self.ground2_posx <= 1:
                self.ground2_posx = 168
            else:
                self. ground2_posx -= Constants.SPEED

            self.update()
            self.draw()

    def update(self):
        if self.pipe_timer == Constants.PIPE_TIMER:
            self.pipes.append(Pipe.Pipe(win))
            self.pipe_timer = 0
        else:
            self.pipe_timer += 1

        for i in range(len(self.pipes)):
            self.pipes[i].update_pipe()

        if self.pipes[0].pos_X <= -100:
            self.pipes.pop(0)

        for i in range(len(self.bird)):
            self.bird[i].update_bird()
            if self.bird[i].is_game_over():
                self.game_over = True

    def draw(self):
        win.blit(Constants.background, (0, 0))

        for i in range(len(self.bird)):
            self.bird[i].draw_bird()

        for i in range(len(self.pipes)):
            self.pipes[i].draw_pipe()

        win.blit(Constants.ground1.convert_alpha(), (self.ground1_posx, self.ground_posy))
        win.blit(Constants.ground2.convert_alpha(), (self.ground2_posx, self.ground_posy))

        pygame.display.flip()
        self.clock.tick(Constants.FPS)


    def start_screen(self):

        icon = pygame.image.load('Assets/elisha.jpg').convert_alpha()

        pygame.display.set_caption('Blappy Fird')
        pygame.display.set_icon(icon)

        run = True
        while run:
            win.blit(Constants.background, (0, 0))
            win.blit(Constants.ground1, (0, 400))
            win.blit(Constants.message, ((Constants.SCREEN_WIDTH - 184) / 2, 90))

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    self.game_over = False
                    self.game_loop()

        pygame.quit()

    def run(self):
        self.start_screen()


if __name__ == '__main__':
    game = Game()
    game.run()

