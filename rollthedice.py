import random
import time

start_time = time.time()
print(" choose an option : 1 roll the dice - 2 exit")


# i = 1
# while i == 1:
while True:
    userChoice = int(input())
    if(userChoice==1):
        print(random.randint(1,6))
    # else if(userChoice==2):
    #     break
    else:
        break

print("--- %s seconds ---" % (time.time() - start_time))