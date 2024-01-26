import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
FRUIT_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Red, Green, Blue

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Fruits Game")

# Player
basket_width = 100
basket_height = 20
basket_x, basket_y = WIDTH // 2 - basket_width // 2, HEIGHT - basket_height - 10
basket_speed = 10

# Fruits
fruit_radius = 20
fruits = []

# Scoring
score = 0
font = pygame.font.Font(None, 36)

# Clock to control the frame rate
clock = pygame.time.Clock()

# Function to generate a random fruit
def generate_fruit():
    color = random.choice(FRUIT_COLORS)
    x = random.randint(fruit_radius, WIDTH - fruit_radius)
    y = -fruit_radius
    return {"x": x, "y": y, "color": color}

# Function to draw a colorful background gradient
def draw_background():
    for y in range(HEIGHT):
        color = (
            int(255 * (y / HEIGHT)),  # Red component
            int(255 * (y / HEIGHT)),  # Green component
            int(255 * (1 - y / HEIGHT)),  # Blue component
        )
        pygame.draw.line(screen, color, (0, y), (WIDTH, y))

# Function to display a button
def draw_button():
    pygame.draw.rect(screen, (0, 255, 0), [WIDTH // 2 - 100, HEIGHT // 2 - 25, 200, 50])
    button_text = font.render("Start Over", True, (255, 255, 255))
    screen.blit(button_text, (WIDTH // 2 - 70, HEIGHT // 2 - 20))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (
                WIDTH // 2 - 100 < mouse_x < WIDTH // 2 + 100
                and HEIGHT // 2 - 25 < mouse_y < HEIGHT // 2 + 25
                and score >= 20
            ):
                # Reset the game if the "Start Over" button is clicked
                score = 0
                fruits.clear()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < WIDTH - basket_width:
        basket_x += basket_speed

    # Move and generate fruits
    for fruit in fruits:
        fruit["y"] += 5
        if (
            basket_x < fruit["x"] < basket_x + basket_width
            and basket_y < fruit["y"] < basket_y + basket_height
        ):
            score += 1
            fruits.remove(fruit)

    # Remove fruits that are off the screen
    fruits = [fruit for fruit in fruits if fruit["y"] < HEIGHT]

    # Generate new fruits randomly
    if random.random() < 0.02:
        fruits.append(generate_fruit())

    # Draw colorful background gradient
    draw_background()

    # Draw everything
    pygame.draw.rect(screen, (255, 255, 255), [basket_x, basket_y, basket_width, basket_height])

    for fruit in fruits:
        pygame.draw.circle(screen, fruit["color"], (fruit["x"], int(fruit["y"])), fruit_radius)

    # Display score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Draw "Start Over" button when the score is 20 or more
    if score >= 20:
        draw_button()

    pygame.display.flip()
    clock.tick(FPS)

# ----------------------------------

# Code Attributtion
# Author.   Sawahat, S.
# Title.    Easy Games in Python
# Date.     February 28, 2021
# Url.      https://www.askpython.com/python/examples/easy-games-in-python
    
# Author.   Mr. Unity Buddy
# Title.    5+ Python Games With Source Code
# Date.     Oct 24, 2021
# Url.      https://dev.to/unitybuddy/5-python-games-with-source-code-3g2b   

# ----------------------------------