import random
import time

start_time = time.time

print('Choose the Length of your password')
userInput = int(input())
passwordGenerated = ""

characters = 'azertyuiopqsdfghjklmwxcvbn0123456789$&.!#@()?*AZERTYUIOPQSDFGHJKLMWXCVBN'
for i in range (0,userInput):
    randomNumber = random.randint(0,70)
    passwordGenerated += characters[randomNumber]
    
print(passwordGenerated)

