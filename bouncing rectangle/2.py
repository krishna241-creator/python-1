import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))

blue = pygame.Rect(50, 150, 60, 60)
red = pygame.Rect(300, 100, 50, 50)

red_dx = random.choice([-5, 5])
red_dy = random.choice([-5, 5])

running = True

while running:
    pygame.time.delay(20)
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        blue.x -= 5
    if keys[pygame.K_RIGHT]:
        blue.x += 5
    if keys[pygame.K_UP]:
        blue.y -= 5
    if keys[pygame.K_DOWN]:
        blue.y += 5

    red.x += red_dx
    red.y += red_dy

    if red.left <= 0 or red.right >= WIDTH:
        red_dx = -red_dx
    if red.top <= 0 or red.bottom >= HEIGHT:
        red_dy = -red_dy

    
    if blue.colliderect(red):
        if blue.width > 10:
            blue.width -= 5
            blue.height -= 5
            blue.x += 2
            blue.y += 2
        else:
            print("GAME OVER")
            running = False

    pygame.draw.rect(screen, (0, 0, 255), blue)
    pygame.draw.rect(screen, (255, 0, 0), red)

    pygame.display.update()

pygame.quit()