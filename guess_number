import random
import time

start_time = time.time()
randomNumber = random.randint(1,50)

print(randomNumber)

guesses = 3

while guesses > 0:
    print("What is your guess between 1 and 50 ?")
    userGuess = int(input())
    while userGuess < 1 or userGuess > 50:
        print('Your choice can not ben outside the interval')
        print("Try again what is your guess between 1 and 50 ?")
        userGuess = int(input())
    if (userGuess != randomNumber):
        guesses = guesses - 1
        if (randomNumber > userGuess):
            print(f"It is more than {userGuess}")
        else:
            print(f'It is less than {userGuess}')
    else:
        print("You find it")
        break
if(guesses == 0):
    print(f"you failed... the right number is : {randomNumber}")

print(" %s seconds" % (time.time() - start_time))
