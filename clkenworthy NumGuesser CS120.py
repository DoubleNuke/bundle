# Sam Kenworthy CS120, 9/12/24
# Number Guesser
import random
randomNum = random.randint(1,100)
attempts = 1
keepGoing = True

while keepGoing == True:
    if attempts != 8:
        print(f"Attempt #{attempts}")
        guess = input("What is your guess? ")
        if  guess.isnumeric() == False:
            print("Guess with a NUMBER, not with LETTERS")
            attempts += 1
        else:
            guess = int(guess)
            if guess > 100:
                print("WAYYYY too high! Stay lower than 100" )
                attempts += 1
            elif guess > randomNum:
                print("Too high! ")
                attempts += 1
            elif guess < randomNum:
                print("Too low! ")
                attempts += 1
            elif guess == randomNum:
                print(f"Nice job! You guessed the number in {attempts} tries! ")
                keepGoing = False
    else:
        print("Too many tries! You lose!")
        print(f"The number was {randomNum}.")
        keepGoing = False
        
print("GAME OVER")