import random

def guess(max_num):
    random_number = random.randint(1,max_num)
    guess = 0
    while guess != random_number :
        guess = int(input(f"Guess a number between 1 and {max_num}. "))
        if guess < random_number:
            print("Guess Again, too low.")
        elif guess > random_number:
            print("Guess Again, too high.")
    print(f"You won!!The correct value was {random_number}")

def computer_guess(max_num):
    low = 1
    high = max_num
    target = int(input(f"Think of a number between {low} and {high}. "))
    guess = 0
    while guess != target:
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = high

        if guess < max_num:
            print(f"Computer guess {guess} is too low")
            low = guess + 1
        elif guess > max_num:
            print(f"Computer guess {guess} is too high")
            high = guess - 1
        
    print('Yaay the computer guessed {guess}, the correct number!')

computer_guess(100)