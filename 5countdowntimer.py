import pygame
import random
import time

# Initialize pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Paddle Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Paddle
paddle_width = 100
paddle_height = 20
paddle_x = screen_width // 2 - paddle_width // 2
paddle_y = screen_height - 50
paddle_speed = 10

# Ball
ball_radius = 10
ball_x = random.randint(ball_radius, screen_width - ball_radius)
ball_y = 100
ball_dx = 5
ball_dy = 5

# Score
score = 0

# Fonts
font = pygame.font.SysFont(None, 36)

# Countdown Timer
countdown = 3

# Game loop
running = True
while running:
    screen.fill(BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT]:
        paddle_x += paddle_speed

    # Ensure paddle stays within the screen boundaries
    if paddle_x < 0:
        paddle_x = 0
    elif paddle_x > screen_width - paddle_width:
        paddle_x = screen_width - paddle_width

    # Move ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Check for collisions with walls
    if ball_x < ball_radius or ball_x > screen_width - ball_radius:
        ball_dx *= -1
    if ball_y < ball_radius:
        ball_dy *= -1

    # Check for collision with paddle
    if ball_y + ball_radius >= paddle_y and paddle_x <= ball_x <= paddle_x + paddle_width:
        ball_dy *= -1
        score += 1

    # Check if ball missed paddle
    if ball_y > screen_height:
        ball_x = random.randint(ball_radius, screen_width - ball_radius)
        ball_y = 100
        score = 0

    # Draw paddle
    pygame.draw.rect(screen, WHITE, (paddle_x, paddle_y, paddle_width, paddle_height))

    # Draw ball
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    # Draw score
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    # Countdown timer
    if countdown > 0:
        countdown_text = font.render("Game starts in: " + str(countdown), True, WHITE)
        screen.blit(countdown_text, (screen_width // 2 - 100, screen_height // 2))
        pygame.display.update()
        time.sleep(1)
        countdown -= 1

    pygame.display.update()
    pygame.time.Clock().tick(60)

pygame.quit()