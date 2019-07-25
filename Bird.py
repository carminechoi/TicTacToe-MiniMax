import pygame
import Constants


class Bird:
    def __init__(self, win, downflap, midflap, upflap):
        self.win = win

        self.bird_x = 120
        self.bird_y = 200

        self.downflap = downflap
        self.midflap = midflap
        self.upflap = upflap
        self.flap = self.midflap
        self.flap_rect = pygame.Rect(self.bird_x, self.bird_y, 34, 24)

        self.flap_count = 0
        self.jump_count = 0
        self.is_jump = False

    def flap_animation(self):
        if self.flap_count == 0:
            self.flap = self.midflap
        elif self.flap_count == 15:
            self.flap = self.downflap
        elif self.flap_count == 30:
            self.flap = self.midflap
        elif self.flap_count == 45:
            self.flap = self.upflap
            self.flap_count = 0
        self.flap_count += 1

    def bird_animation(self, direction):
        if direction == 1:
            if self.flap_count == 0:
                self.flap = self.midflap
            elif self.flap_count == 20:
                self.flap = self.downflap
            elif self.flap_count == 40:
                self.flap = self.midflap
            elif self.flap_count == 60:
                self.flap = self.upflap
                self.flap_count = 0
            self.flap_count += 1

        self.rotate_flap = pygame.transform.rotate(self.flap, self.angle)
        x, y = self.rect.center  # Save its current center.
        self.rect = self.rotate_flap.get_rect()  # Replace old rect with new rect.
        self.rect.center = (x, y)  # Put the new rect's center at old center.
        self.flap = self.rotate_flap

    def jump(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.is_jump = True
            if self.jump_count < 3:
                self.jump_count = 8
        if self.is_jump:
            if self.jump_count >= 0:
                self.bird_y -= (self.jump_count ** 2) * 0.1
                # self.bird_y -= self.jump_count * .6
                self.jump_count -= .25
            else:
                self.jump_count = 8
                self.is_jump = False

    def gravity(self):
        if not self.is_jump:
            self.bird_y += Constants.GRAVITY

    def is_game_over(self):
        if self.bird_y >= Constants.SCREEN_HEIGHT - 130:
            return True

    def update_bird(self):
        self.flap_animation()
        self.jump()
        self.gravity()
        self.flap_rect = pygame.Rect(self.bird_x, self.bird_y, 34, 24)

    def draw_bird(self):
        pygame.draw.rect(self.win, (0, 255, 0), (self.bird_x, self.bird_y, 34, 24))
        self.win.blit(self.flap, (self.bird_x, self.bird_y))
