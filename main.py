import pygame
import time
import random

# Initialize pygame
pygame.init()

# Window size
window_x = 720
window_y = 480

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)  # Red for fruit
green = pygame.Color(0, 255, 0)  # Green for snake
dark_blue = pygame.Color(25, 25, 112)  # Dark blue for background
dark_purple = pygame.Color(48, 25, 52)  # Dark purple for background

# Snake Speed
snake_speed = 15

# Initialize game window
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# Define snake starting position and body
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

# Fruit position
fruit_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]
fruit_spawn = True

# Direction
direction = 'RIGHT'
change_to = direction

# Initial score
score = 0


# Display Score
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)


# Game Over function
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()


# Create a darker gradient background effect
def draw_background():
    for i in range(window_y):
        # Blend between dark blue and dark purple
        blend_factor = i / window_y  # Gradient factor
        r = int(dark_blue.r * (1 - blend_factor) + dark_purple.r * blend_factor)
        g = int(dark_blue.g * (1 - blend_factor) + dark_purple.g * blend_factor)
        b = int(dark_blue.b * (1 - blend_factor) + dark_purple.b * blend_factor)
        color = pygame.Color(r, g, b)
        pygame.draw.line(game_window, color, (0, i), (window_x, i))


# Display Start Screen
def start_screen():
    game_window.fill(black)
    font = pygame.font.SysFont('times new roman', 30)
    start_message = font.render('Press SPACE to Start', True, white)
    start_rect = start_message.get_rect()
    start_rect.center = (window_x / 2, window_y / 2)
    game_window.blit(start_message, start_rect)
    pygame.display.update()


# Main Game Loop
def game_loop():
    global score, snake_position, snake_body, fruit_position, direction, change_to, fruit_spawn

    # Define snake starting position and body
    snake_position = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

    # Fruit position
    fruit_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]
    fruit_spawn = True

    # Direction
    direction = 'RIGHT'
    change_to = direction

    # Initial score
    score = 0

    # Main Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'

        # If two keys pressed simultaneously, we don't want snake to move into two directions simultaneously
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Moving the snake
        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        # Snake body growing mechanism
        snake_body.insert(0, list(snake_position))
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 10
            fruit_spawn = False
        else:
            snake_body.pop()

        if not fruit_spawn:
            fruit_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]

        fruit_spawn = True
        game_window.fill(black)  # Fill background with black for now

        # Drawing background gradient
        draw_background()

        # Drawing snake
        for segment in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(segment[0], segment[1], 10, 10))  # Snake body (green squares)

        # Drawing fruit
        pygame.draw.rect(game_window, red, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))  # Red fruit

        # Game Over conditions
        if snake_position[0] < 0 or snake_position[0] > window_x - 10:
            game_over()
        if snake_position[1] < 0 or snake_position[1] > window_y - 10:
            game_over()

        # Touching the snake body
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over()

        # Displaying score continuously
        show_score(1, white, 'times new roman', 20)

        # Refresh game screen
        pygame.display.update()

        # Frame Per Second / Refresh Rate
        fps.tick(snake_speed)


# Start Screen Loop
def game_start():
    while True:
        start_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()  # Start the game when SPACE is pressed


# Run the game
game_start()
