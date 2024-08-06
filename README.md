---

# Number Guessing Game

## Project Overview

The Number Guessing Game is a simple console-based game where the player tries to guess a randomly selected number within a specified range. The game provides feedback on whether the guess is too high or too low and tracks the number of attempts taken to guess the correct number. This project is designed to help beginners practice basic Python programming concepts such as loops, conditionals, and user input.

## Features

- **Random Number Generation**: The computer randomly selects a number between 1 and 100.
- **User Interaction**: The user guesses the number and receives feedback on their guesses.
- **Attempt Tracking**: Counts the number of guesses made to find the correct number.
- **Replay Option**: Allows the user to play multiple rounds of the game.

## Installation

No special installation is required. This project is compatible with Python 3.x. Ensure that Python is installed on your computer.

## Getting Started

### File Structure

Create a directory for your project and navigate into it. Inside the directory, create a Python file named `number_guessing_game.py`.

### Project Code

Save the following code in the `number_guessing_game.py` file:

```python
# number_guessing_game.py

import random

def display_welcome_message():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

def get_random_number():
    return random.randint(1, 100)

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            return guess
        except ValueError:
            print("Please enter a valid integer.")

def provide_feedback(number, guess):
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number!")

def play_game():
    number = get_random_number()
    attempts = 0
    guess = None
    
    while guess != number:
        guess = get_user_guess()
        attempts += 1
        provide_feedback(number, guess)
    
    print(f"It took you {attempts} attempts to guess the number.")

def main():
    display_welcome_message()
    
    while True:
        play_game()
        replay = input("Do you want to play again? (yes/no): ").strip().lower()
        if replay != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
```

### Running the Project

1. Save the code above in a file named `number_guessing_game.py`.
2. Open your terminal or command prompt.
3. Navigate to the directory where `number_guessing_game.py` is saved.
4. Run the script using Python:
   ```bash
   python number_guessing_game.py
   ```

### Usage

1. **Start the Game**: The game will prompt you to guess a number between 1 and 100.
2. **Make a Guess**: Enter a number and press Enter.
3. **Receive Feedback**: The game will indicate if your guess is too low or too high.
4. **Guess Again**: Continue guessing until you find the correct number.
5. **End the Game**: After guessing the number, the game will display the number of attempts.
6. **Replay Option**: You can choose to play again or exit the game.

## Tips for Enhancement

- **Difficulty Levels**: Implement different difficulty levels with varying ranges (e.g., 1-50, 1-100, 1-1000).
- **Hints**: Provide additional hints based on the number of attempts.
- **High Scores**: Track high scores or the minimum number of attempts taken.

## License

This project is for educational purposes and is provided as-is. Feel free to modify and use it according to your needs.

## Contact

For questions or feedback, you can reach out to:

- **Your Name**: [your.email@example.com]

---

