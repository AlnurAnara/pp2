import random

def guess_the_number():
    # Randomly choose a number between 1 and 20
    number_to_guess = random.randint(1, 20)
    
    # Ask for the player's name
    name = input("Hello! What is your name?\n")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    # Initialize the number of guesses
    guesses_taken = 0
    
    while True:
        # Ask for the player's guess
        guess = int(input("Take a guess.\n"))
        guesses_taken += 1
        
        # Check if the guess is too low, too high, or correct
        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break  # Exit the loop once the correct number is guessed

guess_the_number()

'''
Write a program able to play the "Guess the number" - game
where the number to be guessed is randomly chosen between 1 and 20.
'''