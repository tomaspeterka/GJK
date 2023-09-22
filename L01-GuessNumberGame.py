import random

while True:
    thought_number = random.randint(1, 100)  # Generate a random number between 1 and 100

    while True:

        idea = int(input("What do you think is my number: "))

        if idea > thought_number:
            print("It's less")

        elif idea < thought_number:
            print("It's more")

        elif idea == thought_number:
            print(f"You guessed it. My number was {thought_number}!")
            break  # Exit the inner loop when the correct number is guessed

    next_game = input("Do you want to play again? (yes/no): ")

    if next_game.lower() != "yes":
        break  # Exit the loop if the user doesn't want to play again

    thought_number = random.randint(1, 100)  # Generate a new random number for the next game

print("Thanks for playing!")
print("Created by TomCODES")
