import pygame
import Constants

import math

class Bird:
    def __init__(self, win, downflap, midflap, upflap):
        self.win = win

        self.bird_x = Constants.BIRD_X
        self.bird_y = Constants.BIRD_Y

        self.downflap = downflap
        self.midflap = midflap
        self.upflap = upflap
        self.flap = self.midflap
        self.flap_rect = pygame.Rect(self.bird_x, self.bird_y, 34, 24)

        self.direction = 0
        self.rotate = False

        self.flap_count = 0
        self.jump_count = 0
        self.is_jump = False

    # cycle through flap images
    def flap_animation(self):
        if self.rotate:
            self.direction = 30
        elif self.direction > -90:
            self.direction -= math.sqrt(abs(self.direction)) * 0.3
        if self.flap_count == 0:
            self.flap = self.midflap
            self.bird_animation(self.direction)
        elif self.flap_count == 15:
            self.flap = self.downflap
            self.bird_animation(self.direction)
        elif self.flap_count == 30:
            self.flap = self.midflap
            self.bird_animation(self.direction)
        elif self.flap_count == 45:
            self.flap = self.upflap
            self.bird_animation(self.direction)
            self.flap_count = 0
        self.flap_count += 1

    # STILL NEEDS WORK
    # handles bird rotation animation
    def bird_animation(self, angle):
        rotate_flap = pygame.transform.rotate(self.flap, angle)
        rect = pygame.Rect(self.bird_x, self.bird_y, 34, 24)
        x, y = rect.center  # Save its current center.
        rect = rotate_flap.get_rect()  # Replace old rect with new rect.
        rect.center = (x, y)  # Put the new rect's center at old center.
        self.flap = rotate_flap

    # jump if 'space' is pressed
    def jump(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.is_jump = True
            self.rotate = True
            if self.jump_count < 3:
                self.jump_count = 8
        if self.is_jump:
            if self.jump_count >= 0:
                # jump based on quadratic equation for hang time effect
                self.bird_y -= (self.jump_count ** 2) * 0.1
                self.jump_count -= .25
                if self.jump_count <= 2:
                    self.rotate = False
            else:
                self.jump_count = 8
                self.is_jump = False

    # drops brid when it's not jumping by GRAVITY amount
    def gravity(self):
        if not self.is_jump:
            self.bird_y += Constants.GRAVITY

    # if bird reaches the ground, end game
    def is_game_over(self):
        if self.bird_y >= Constants.SCREEN_HEIGHT - 130:
            self.bird_y = Constants.BIRD_Y
            return True

    def update_bird(self):
        self.flap_animation()
        self.jump()
        self.gravity()
        self.flap_rect = pygame.Rect(self.bird_x, self.bird_y, 34, 24)

    def draw_bird(self):
        # for collision testing
        # pygame.draw.rect(self.win, (0, 255, 0), (self.bird_x, self.bird_y, 34, 24))
        self.win.blit(self.flap, (self.bird_x, self.bird_y))
