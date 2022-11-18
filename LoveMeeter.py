#lets see whos right :)
import random
import time

   
print("As we all gather here to see the age old answer.")
print("Who loves the other person more.")
time.sleep(4)

xerenity = random.randint(1,9)
elitey = random.randint(1,9)

print("Elite first lets see your number first!")
time.sleep(1)

print(elitey)
time.sleep(1)

print("Xerenity now your turn!")
time.sleep(1)

print(xerenity)
time.sleep(1)

if xerenity > elitey:
    print("What an outcome folks! I but i think we all knew that was going to happen.")
elif xerenity < elitey:
    print("Whoa! What a turn of events! How can this be?!?! IT SHOULD BE IMPOSSIBLE!!")
elif xerenity == elitey:
    print("WHAT! theres no way its gotta be a mistake!")