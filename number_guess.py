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
