import pygame
SCREEN_WIDTH = 100
SCREEN_HEIGHT = 100

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

while True:
    print('gameloop') 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    screen.fill("pink")
    pygame.display.filp()
    clock.tick(60)
