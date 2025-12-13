import random
playing = True
number = str(random.randint(1,10))

print("-> generating a random number from 1 to 10")
print("-> the game ends when you get ONE point")

while playing:
    guess = input("guess the number: \n")
    if number == guess:
        print("> you win the game")
        print("> the number was", number)
        break

    else:
        print("> you lost, try again")
        print("> the number was", number)