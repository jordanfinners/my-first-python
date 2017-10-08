import random

number = random.randint(0,100)


def guess_this_number():
    guess = input("Guess the number ")

    try:
        guess_input = int(guess)
        if guess_input == number:
            print("Correct!!")
        elif guess_input > number:
            print("Your guess is {}!".format("too high"))
            guess_this_number()
        else:
            print("Your guess is too low!")
            guess_this_number()
    except:
        print("Whoops looks like that isn't a number!")


guess_this_number()