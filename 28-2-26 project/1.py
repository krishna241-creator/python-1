import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    pygame.draw.rect(screen,(255,255,0), pygame.Rect(100,100,125,75))
    pygame.display.flip()
    