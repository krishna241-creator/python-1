import pygame
import random
import time
import os

pygame.init()

# Screen
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Catch the Red Square!")

# Colors
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

# Player and target
player_size = 50
player_x, player_y = width//2, height//2
target_size = 30
target_x, target_y = random.randint(0, width-target_size), random.randint(0, height-target_size)
target_dx, target_dy = 3, 3
player_speed = 5

# Score & timer
score = 0
font = pygame.font.SysFont(None, 36)
start_time = time.time()
game_duration = 60

# Leaderboard
leaderboard_file = "leaderboard.txt"
if os.path.exists(leaderboard_file):
    with open(leaderboard_file, "r") as f:
        leaderboard = [int(line.strip()) for line in f.readlines()]
else:
    leaderboard = []

clock = pygame.time.Clock()
running = True
game_over = False

while running:
    clock.tick(60)
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_UP]:
            player_y -= player_speed
        if keys[pygame.K_DOWN]:
            player_y += player_speed
        player_x = max(0, min(width - player_size, player_x))
        player_y = max(0, min(height - player_size, player_y))

        # Target movement with random jitter
        target_x += target_dx + random.choice([-1, 0, 1])
        target_y += target_dy + random.choice([-1, 0, 1])

        # Bounce with slight random direction change
        if target_x <= 0 or target_x >= width - target_size:
            target_dx *= -1
            target_dx += random.choice([-1, 0, 1])
        if target_y <= 0 or target_y >= height - target_size:
            target_dy *= -1
            target_dy += random.choice([-1, 0, 1])

        # Collision check
        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
        target_rect = pygame.Rect(target_x, target_y, target_size, target_size)
        if player_rect.colliderect(target_rect):
            score += 1
            target_x, target_y = random.randint(0, width-target_size), random.randint(0, height-target_size)
            # Increase speed with random direction
            target_dx += 1 if target_dx > 0 else -1
            target_dy += 1 if target_dy > 0 else -1
            # Randomly flip direction
            if random.random() < 0.5:
                target_dx *= -1
            if random.random() < 0.5:
                target_dy *= -1

        # Timer check
        if time.time() - start_time >= game_duration:
            game_over = True
            leaderboard.append(score)
            leaderboard.sort(reverse=True)
            leaderboard = leaderboard[:5]
            with open(leaderboard_file, "w") as f:
                for s in leaderboard:
                    f.write(f"{s}\n")

    # Draw target and player
    if not game_over:
        pygame.draw.rect(screen, red, (target_x, target_y, target_size, target_size))
    pygame.draw.rect(screen, blue, (player_x, player_y, player_size, player_size))

    # Score and timer
    score_text = font.render(f"Score: {score}", True, black)
    screen.blit(score_text, (10, 10))
    time_left = max(0, int(game_duration - (time.time() - start_time)))
    timer_text = font.render(f"Time: {time_left}", True, black)
    screen.blit(timer_text, (450, 10))

    # Leaderboard
    if game_over:
        game_over_text = font.render("Time's up! Leaderboard:", True, black)
        screen.blit(game_over_text, (150, 150))
        for i, s in enumerate(leaderboard):
            lb_text = font.render(f"{i+1}. {s}", True, black)
            screen.blit(lb_text, (200, 180 + i*30))

    pygame.display.update()