i = 0
while i <= 10:
    print("i is now {}".format(i))
    i += 1

# Must initialize variable for while loops and condition mut eventually become false for loop to end.#

availableExits = ["east", "north east", "south"]

chosenExit = ""
while chosenExit not in availableExits:
    chosenExit = input("Please chose a direction: ")
    if chosenExit == "quit":
        print("Game Over")
        break
else:
    print("You went {}".format(chosenExit))


##Challenge Problem##

import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}".format(highest))
guess = 0

while guess != answer:
    guess = int(input())
    if guess == 0:
        break
    if guess < answer:
        print("Guess higher")
    elif guess > answer:
        print("Guess lower")

else:
    print("You got it!")
