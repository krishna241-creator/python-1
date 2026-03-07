import pygame
import random

screen = pygame.display.set_mode((1280,1000))

bg_color = [(0,0,0),(255,255,255),(168,241,222)]
sp_color = [(0,255,0),(0,0,255),(255,0,0)]

bg = bg_color[0]
sp = sp_color[0]

x = 50
y = 50
width = 30
height = 20

vx = 2
vy = 2

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
    
    x += vx
    y += vy

    if x <= 0 or x + width >= 500:
        vx = -vx
        sp = random.choice(sp_color)
        bg = random.choice(bg_color)

    if y <= 0  or y + height >= 400:
        vy = -vy
        sp = random.choice(sp_color)
        bg = random.choice(bg_color)

    screen.fill(bg)
    pygame.draw.rect(screen, sp, (x, y, width, height))

    pygame.display.flip()
    clock.tick(80)

pygame.quit()