# Pong Game

This is a simple implementation of the classic Pong game using Python's `turtle` module. The game features a ball, paddles, a scoreboard, and basic controls for two players.

## Project Files

- **Ball.py**: Contains the `Ball` class, which handles the movement and behavior of the ball.
- **Paddle.py**: Contains the `Paddle` class, which represents the paddles controlled by players.
- **Scoreboard.py**: Contains the `Scoreboard` class, which keeps track of and displays the score.
- **Main.py**: The main game file, which initializes the screen, the ball, paddles, and scoreboard, and controls the game loop.

## Requirements

This project requires Python and the `turtle` module. The `turtle` module is built into Python, so no additional installation is required.

## Installation

1. Clone the repository to your local machine:
   ```bash
   gh repo clone ulquiorraexe/pong
2. Navigate to the project directory:
   ```bash
   cd pong
3. Run the `main.py` file to start the game:
   ```bash
   python main.py

## Gameplay

- The game is played with two paddles controlled by two players.
- Player 1 controls the right paddle using the `Up` and `Down` arrow keys.
- Player 2 controls the left paddle using the `W` and `S` keys.
- The ball bounces off the top and bottom of the screen.
- When the ball hits a paddle, it bounces back in the opposite direction.
- When the ball passes a paddle (goes off the left or right side of the screen), the opponent scores a point.
- The first player to score a set number of points (e.g., 10) wins the game.

## Notes

- The ball starts with a random speed and direction.
- The game continues in a loop until the user closes the window.
- The paddles are restricted to vertical movement within the screen boundaries.
- The game doesn't include any AI for a single-player mode, so it's intended for two players.
- The scoreboard updates every time a player scores a point, showing both the left and right player scores.

## License

This project is not licensed. 
