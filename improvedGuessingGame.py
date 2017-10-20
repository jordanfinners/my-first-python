import random

number = random.randint(0, 100)
guesses = 1

while True:
    print("Guess the number...")
    guess = input()
    try:
        guess_input = int(guess)
        if guess_input == number:
            print("Correct!! You guessed it in {} guesses".format(guesses))
            break
        elif guess_input > number:
            print("Too high!")
        else:
            print("Too low!")
    except ValueError:
        print("Whoops that's not a number, try again")
    guesses += 1

