# Snakes
Simple snake game using pygame

A simple implementation of the classic Snake game using Python and Pygame. The game features a snake that moves around the screen to collect food (red fruit) while avoiding collisions with the screen boundaries and the snake's body. The player controls the snake using the arrow keys, and the game displays the current score. The game begins with a start screen prompting the player to press the `Space` key to start.

## Features:
- **Start Screen**: Press `Space` to start the game.
- **Snake Movement**: Use arrow keys to control the direction of the snake.
- **Food Collection**: The snake grows longer each time it eats a piece of red fruit.
- **Score Tracking**: The player's score increases by 10 points each time the snake eats food.
- **Game Over Conditions**: The game ends if the snake collides with the boundaries or its own body.

## Requirements:

- Python 3.x
- Pygame library

To install Pygame, you can use pip:

```bash
pip install pygame
```

## How to Play:
1. Clone the repository:
   ```bash
   git clone https://github.com/Fardeen2903/Snakes.git
   cd snake-game
   ```
2. Run the game:
   ```bash
   python main.py
   ```
3. On the start screen, press the `Space` key to start the game.
4. Use the arrow keys (`Up`, `Down`, `Left`, `Right`) to control the snake.
5. The game will end if the snake collides with the walls or itself.
6. The score is displayed at the top left corner of the screen.

## License:

This project is licensed under the BSD 2-Clause License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments:
- This project was created as a simple example of a Snake game using Pygame.
- Thanks to the Pygame community for the resources and tutorials that made this possible.
