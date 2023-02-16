import random

x=int(input("Enter lower bound: "))
y=int(input("Enter upper bound: "))

n = random.randrange(x,y)
guess = int(input("Enter any number: "))

while n!= guess:

    if guess < n:
        print("Too low")
        guess = int(input("Enter number again: "))

    elif guess > n:
        print("Too high!")
        guess = int(input("Enter number again: "))

    else:
      break
    
print("You guessed it right!")