import pygame
import random

# Initialize Pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 15
FPS = 60
SKY_BLUE = (135, 206, 235)
BLACK = (0, 0, 0)

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Create paddles
player1_paddle = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Create ball
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_speed = [5 * random.choice([1, -1]), 5 * random.choice([1, -1])]

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_paddle.top > 0:
        player1_paddle.y -= 5
    if keys[pygame.K_s] and player1_paddle.bottom < HEIGHT:
        player1_paddle.y += 5
    if keys[pygame.K_UP] and player2_paddle.top > 0:
        player2_paddle.y -= 5
    if keys[pygame.K_DOWN] and player2_paddle.bottom < HEIGHT:
        player2_paddle.y += 5

    # Update ball position
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Ball collision with walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] = -ball_speed[1]
    if ball.colliderect(player1_paddle) or ball.colliderect(player2_paddle):
        ball_speed[0] = -ball_speed[0]

    # Ball out of bounds (score)
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed[0] = -ball_speed[0]
        ball.center = (WIDTH // 2, HEIGHT // 2)

    # Clear the screen
    screen.fill(SKY_BLUE)

    # Draw paddles and ball
    pygame.draw.rect(screen, BLACK, player1_paddle)
    pygame.draw.rect(screen, BLACK, player2_paddle)
    pygame.draw.ellipse(screen, BLACK, ball)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
