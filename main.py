import random
import art
Easy_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Guess is too high.")
        return turns - 1
    elif guess < answer:
        print("Guess is too low.")
        return turns - 1
    else:
        print(f"You guessed the correct number. The answer is {answer}")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return Easy_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
def game():
    print(art.logo3)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts left to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer,turns)
        if turns == 0:
            return
        elif guess != answer:
            print("guess again.")
game()
