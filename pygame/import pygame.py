import pygame
pygame.init()
screen = pygame.display.set_mode((720,810))
game = False
while not game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = True
    
    pygame.display.flip()

