

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
        ###   LOADING IMAGE ASSETS   ###
        self.background = pygame.image.load('Assets/background.png').convert_alpha()
        self.background = pygame.transform.scale(self.background, (Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))

        self.ground1 = pygame.image.load('Assets/ground.png').convert_alpha()
        self.ground2 = pygame.image.load('Assets/ground.png').convert_alpha()

        self.message = pygame.image.load('Assets/message1.png').convert_alpha()

        self.downflap = pygame.image.load('Assets/bluebird-downflap.png').convert_alpha()
        self.midflap = pygame.image.load('Assets/bluebird-midflap.png').convert_alpha()
        self.upflap = pygame.image.load('Assets/bluebird-upflap.png').convert_alpha()

        self.lower_pipe = pygame.image.load('Assets/pipe.png').convert_alpha()
        self.upper_pipe = pygame.image.load('Assets/pipe.png').convert_alpha()
        self.upper_pipe = pygame.transform.rotate(self.upper_pipe, 180)

        self.zero = pygame.image.load('Assets/0.png').convert_alpha()
        self.one = pygame.image.load('Assets/1.png').convert_alpha()
        self.two = pygame.image.load('Assets/2.png').convert_alpha()
        self.three = pygame.image.load('Assets/3.png').convert_alpha()
        self.four = pygame.image.load('Assets/4.png').convert_alpha()
        self.five = pygame.image.load('Assets/5.png').convert_alpha()
        self.six = pygame.image.load('Assets/6.png').convert_alpha()
        self.seven = pygame.image.load('Assets/7.png').convert_alpha()
        self.eight = pygame.image.load('Assets/8.png').convert_alpha()
        self.nine = pygame.image.load('Assets/9.png').convert_alpha()
        ### ----------------------- ###

        self.score = 0

        self.ground1_posx = -168
        self.ground2_posx = 168
        self.ground_posy = 400

        # initialize bird object
        self.bird = list()
        self.bird.append(Bird.Bird(win, self.downflap, self.midflap, self.upflap))

        #initialize pipe object
        self.pipes = list()
        self.pipes.append(Pipe.Pipe(win, self.lower_pipe, self.upper_pipe))

        self.pipe_timer = 0

        self.game_over = False

        self.clock = pygame.time.Clock()

    def draw_score(self):
        # break score into single digits
        score = [int(i) for i in str(self.score)]
        length = len(score)

        # draw score accordingly
        for i in range(length):
            if score[i] == 0:
                win.blit(self.zero, (Constants.SCORE_WIDTH / 2 + ((i * 2.2) * 12), Constants.SCORE_HEIGHT))
            elif score[i] == 1:
                win.blit(self.one, (Constants.SCORE_WIDTH / 2 + ((i * 2.2) * 12 + 8), Constants.SCORE_HEIGHT))
            elif score[i] == 2:
                win.blit(self.two, (Constants.SCORE_WIDTH / 2 + ((i * 2.2) * 12), Constants.SCORE_HEIGHT))
            elif score[i] == 3:
                win.blit(self.three, (Constants.SCORE_WIDTH / 2 + ((i * 2.2) * 12), Constants.SCORE_HEIGHT))
            elif score[i] == 4:
                win.blit(self.four, (Constants.SCORE_WIDTH / 2 + ((i * 2.2) * 12), Constants.SCORE_HEIGHT))
            elif score[i] == 5:
                win.blit(self.five, (Constants.SCORE_WIDTH / 2 + ((i * 2.2) * 12), Constants.SCORE_HEIGHT))
            elif score[i] == 6:
                win.blit(self.six, (Constants.SCORE_WIDTH / 2 + ((i * 2.2) * 12), Constants.SCORE_HEIGHT))
            elif score[i] == 7:
                win.blit(self.seven, (Constants.SCORE_WIDTH / 2 + ((i * 2.2) * 12), Constants.SCORE_HEIGHT))
            elif score[i] == 8:
                win.blit(self.eight, (Constants.SCORE_WIDTH / 2 + ((i * 2.2) * 12), Constants.SCORE_HEIGHT))
            elif score[i] == 9:
                win.blit(self.nine, (Constants.SCORE_WIDTH / 2 + ((i * 2.2) * 12), Constants.SCORE_HEIGHT))

    # main game loop
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
        # controlls pipe spawning
        if self.pipe_timer == Constants.PIPE_TIMER:
            self.pipes.append(Pipe.Pipe(win, self.lower_pipe, self.upper_pipe))
            self.pipe_timer = 0
        else:
            self.pipe_timer += 1
        # remove pipe when its offscreen
        if self.pipes[0].pos_X <= -100:
            self.pipes.pop(0)

        # update each pipe and check collision
        for i in range(len(self.pipes)):
            self.pipes[i].update_pipe()
            if self.pipes[i].is_collision(self.bird[0]):
                self.game_over = True
                break
            elif self.pipes[i].pos_X == Constants.BIRD_X - 17:
                self.score += 1

        # update each bird
        for i in range(len(self.bird)):
            self.bird[i].update_bird()
            if self.bird[i].is_game_over():
                self.game_over = True

    def draw(self):
        # draw background
        win.blit(self.background, (0, 0))

        # draw each bird
        for i in range(len(self.bird)):
            self.bird[i].draw_bird()

        # draw each pipe
        for i in range(len(self.pipes)):
            self.pipes[i].draw_pipe()

        # draw ground over pipe
        win.blit(self.ground1, (self.ground1_posx, self.ground_posy))
        win.blit(self.ground2, (self.ground2_posx, self.ground_posy))

        # draw score
        self.draw_score()

        # update the screen
        pygame.display.flip()
        self.clock.tick(Constants.FPS)

    def start_screen(self):

        icon = pygame.image.load('Assets/elisha.jpg')

        pygame.display.set_caption('Blappy Fird')
        pygame.display.set_icon(icon)

        run = True
        while run:
            win.blit(self.background, (0, 0))
            win.blit(self.ground1, (0, 400))
            win.blit(self.message, ((Constants.SCREEN_WIDTH - 184) / 2, 90))

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    self.game_over = False
                    self.__init__()
                    self.game_loop()

        pygame.quit()

    def run(self):
        self.start_screen()


if __name__ == '__main__':
    game = Game()
    game.run()

