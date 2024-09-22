import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Secret Number Guessing Game!!!")
    print("I have selected a number between 1 and 100.")
    print("Can you guess what that number it is???")

    while True:
        guess = input("Enter your guess: ")

        if not guess.isdigit():
            print("Invalid input! Please enter a valid number between 1 and 100.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < 1 or guess > 100:
            print("Your guess is out of range! Please enter a number between 1 and 100.")
        elif guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
            break
        
print(guess_the_number())