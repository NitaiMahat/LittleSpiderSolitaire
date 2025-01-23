# Little Spider Solitaire

## Overview
This project implements a version of **Little Spider Solitaire**, a card game where the objective is to move all cards to the foundation piles, building them sequentially by suit. The game is designed with an interactive graphical interface.

## Game Rules
- The game begins with foundation piles starting with two red aces and two black kings.
- Cards can be moved from:
  - Tableau to foundation piles (if it follows the sequential rule).
  - One tableau to another (if ranks differ by ±1 or it's an empty tableau).
- Clicking the stock pile deals eight more cards if no valid moves are available.
- A point is earned for every valid move to a foundation pile.
- The game ends when all cards are in the foundation piles or the player chooses to quit.

## Files
- **Final_Little_Spider_Solitaire.py**: Main program file.
- **board.py**: Manages the game board and card placements.
- **button.py**: Handles interactive buttons in the game.
- **card.py**: Represents individual card properties and behavior.
- **deck.py**: Handles card deck creation and shuffling.
- **graphics2.py**: Provides graphical functionalities.

## Features
- Interactive game interface with user-friendly controls.
- Real-time scoring system.
- Pop-up windows for game directions, gameplay, and game over messages.
- Validates all moves to ensure adherence to the game rules.

## How to Play
1. Run `Final_Little_Spider_Solitaire.py` to start the game.
2. Follow the instructions displayed in the "Directions" window.
3. Make moves by clicking cards and tableau piles.
4. Click the stock pile to deal more cards if no valid moves exist.
5. Enjoy the game and aim for a high score!

## Requirements
- Python 3.x
- `graphics.py` (Ensure it's installed in your Python environment)

## Credits
Developed by **Nitai Mahat**.  

Enjoy the challenge of Little Spider Solitaire! 🕷️♠️♥️
