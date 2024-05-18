import random
def guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it!")
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter an integer.")
if __name__ == "__main__":
    guessing_game()



