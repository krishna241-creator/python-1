# section - 1
import pygame
pygame.init()

# section - 2
screen = pygame.display.get((640,480))
caption = pygame.display.set_caption("this is my first game")

# section - 3
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)

# section - 4
font = pygame.display.SysFont(40)
text = font.render("my game screen",True,BLACK)

# section - 5
running = True

#section - 6
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# section - 7
    screen.fill(WHITE)
    pygame.draw.rect(BLUE,True,pygame.rect(220,190,200,100))
    screen.blit(text,text.get_rect(center = (320,50)))
    pygame.display.flip()

pygame.QUIT()