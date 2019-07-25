import pygame

SCREEN_WIDTH = 336
SCREEN_HEIGHT = 512
SPEED = 1
FPS = 120
PIPE_TIMER = 180
GRAVITY = 3

background = pygame.image.load('Assets/background.png')
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

ground1 = pygame.image.load('Assets/ground.png')
ground2 = pygame.image.load('Assets/ground.png')

message = pygame.image.load('Assets/message.png')

downflap = pygame.image.load('Assets/bluebird-downflap.png')
midflap = pygame.image.load('Assets/bluebird-midflap.png')
upflap = pygame.image.load('Assets/bluebird-upflap.png')

lower_pipe = pygame.image.load('Assets/pipe.png')
upper_pipe = pygame.image.load('Assets/pipe.png')
upper_pipe = pygame.transform.rotate(upper_pipe, 180)
