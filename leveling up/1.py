import pygame
import random

pygame.init()

width = 600
height = 500

screen = pygame.display.set_mode((width,height))

pygame.display.set_caption("Leveled up game")

bg = pygame.image.load("images.jfif")
bg = pygame.transform.scale(bg,(width,height))

font = pygame.font.SysFont("Times New Roman",60)

player = pygame.Rect(random.randint(0,470), random.randint(0,380), 30, 20)
enemy = pygame.Rect(random.randint(0,470), random.randint(0,380), 30, 20)

speed = 8
won = False
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not won:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            player.x += speed
        if keys[pygame.K_LEFT]:
            player.x -= speed
        if keys[pygame.K_UP]:
            player.y -= speed
        if keys[pygame.K_DOWN]:
            player.y += speed

        if player.x < 0 :
            player.x = 0
        if player.x > width - 30:
            player.x = width - 30
        if player.y < 0 :
            player.y = 0
        if player.y > height - 20:
            player.y = height - 20

        if player.colliderect(enemy):
            won = True
         
    screen.blit(bg,(0,0))    
    pygame.draw.rect(screen,(0,0,255),player)
    pygame.draw.rect(screen,(255,0,0),enemy)

    if won:
        text = font.render("You win!",True,(0,0,0))
        screen.blit(text,(170,170))

    pygame.display.update()
    clock.tick(60)

pygame.quit()      