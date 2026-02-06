import random

secret = random.randint(1,50)
guess = 0

while secret != guess:
    guess = int(input("Guess a number between 1 and 50: "))
    if(guess < secret):
        print("Too low! Try again.")
    elif(guess > secret):
        print("Too high! Try again.")
    
print("Congratulations! You guessed the number.")