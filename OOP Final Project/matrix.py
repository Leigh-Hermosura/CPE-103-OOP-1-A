import pygame
import random
import sys

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
FONT_SIZE = 20
FPS = 60

# Colors
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Matrix Rain")
font = pygame.font.SysFont("consolas", FONT_SIZE, bold=True)
clock = pygame.time.Clock()

# Characters and columns
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*"
columns = WIDTH // FONT_SIZE
drops = [random.uniform(0, HEIGHT // FONT_SIZE) for _ in range(columns)]
last_rows = [-1] * columns  # Track last drawn row per column

# Fade surface
fade_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

# Rain speed
# kapag mababa ung speed (ex. RAIN_SPEED = 5) dapat iadjust mo rin ung fade speed dun kunyari fade_surface.fill((0, 0, 0, 9))
# vice versa naman kapag mabilis (ex. RAIN_SPEED = 50) dapat mas mabilis magfade, kunyari fade_surface.fill((0, 0, 0, 40))
RAIN_SPEED = 9

running = True
while running:
    dt = clock.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fading overlay
    fade_surface.fill((0, 0, 0, 13))  # Adjust fade strength here
    screen.blit(fade_surface, (0, 0))

    # Draw characters per column
    for i in range(columns):
        current_row = int(drops[i])

        if current_row != last_rows[i]:
            x = i * FONT_SIZE
            y = current_row * FONT_SIZE

            if y < HEIGHT:
                char = random.choice(chars)
                char_surface = font.render(char, True, GREEN)
                screen.blit(char_surface, (x, y))
                last_rows[i] = current_row

        drops[i] += RAIN_SPEED * dt

        if drops[i] * FONT_SIZE > HEIGHT and random.random() > 0.975:
            drops[i] = 0
            last_rows[i] = -1  # Reset tracking

    pygame.display.flip()

pygame.quit()
sys.exit()
