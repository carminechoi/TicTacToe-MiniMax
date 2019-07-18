

# Carmine Choi
# July 16, 2019

import os
import pygame


# Global Variables

SCREEN_WIDTH = 288
SCREEN_HEIGHT = 512

def game_loop():
    print("hello")


def main_menu():

    win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    background = pygame.image.load('Assets/background.png')
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    ground = pygame.image.load('Assets/ground.png')
    ground = pygame.transform.scale(ground, (SCREEN_WIDTH, 112))

    icon = pygame.image.load('Assets/elisha.jpg')

    pygame.display.set_caption('Blappy Fird')
    pygame.display.set_icon(icon)

    run = True
    while run:
        win.blit(background, (0, 0))
        win.blit(ground, (0, 400))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                print("Hello World")
    pygame.quit()


main_menu()



# class Window:
#     def __init__(self):
#         self.x = 100
#         self.y = 50
#         self.width = 540
#         self.height = 960
#         self.win = pygame.display.set_mode((self.width, self.height))
#
#     def display(self):
#         os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (self.x, self.y)
#
#         icon = pygame.image.load('elisha.jpg')
#
#         pygame.display.set_caption("Blappy Fird")
#         pygame.display.set_icon(icon)
#
# class Blappy:
#     def __init__(self):
#         self.x = 50
#         self.y = 440
#         self.width = 50
#         self.height = 50
#         self.vel = 10
#
#     def checkKeyPress(self):
#         keys = pygame.key.get_pressed()
#
#         if keys[pygame.K_SPACE]:
#             self.y += self.vel
#
#     def updateBlappy(self):
#         pygame.draw.rect(self.win, (255, 0, 0), (self.x, self.y, self.width, self.height))
#
#
# # set window starting position (x,y)
#
# window = Window()
# blappy = Blappy()
#
# window.display()
# run = True
# while run:
#     pygame.time.delay(50)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#
#     blappy.checkKeyPress()
#
#     # Update Block
#     win.fill((0, 0, 0))
#     blappy.updateBlappy()
#
#     pygame.display.update()
#
# pygame.quit()
