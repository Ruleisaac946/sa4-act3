number = 10
max_guesses = 5  
remaining_guesses = max_guesses  

print("I'm thinking of a number...")
while remaining_guesses > 0:
    guess = input(f"What number am I thinking of? You have {remaining_guesses} guesses left. (Enter 'q' to quit) ")
    if guess == 'q':
        print(f"The number was {number}.")
        break
    try:
        guess = int(guess)
        if guess == number:
            print("Congratulations! You guessed the right number.")
            break
        elif guess < number:
            print("Sorry! Your guess was too low.")
        else:
            print("Sorry! Your guess was too high.")
        remaining_guesses -= 1  # Decrement remaining guesses
        if remaining_guesses == 0:
            print(f"Out of guesses! The number was {number}.")
            break
    except ValueError:
        print("Please enter a valid number or 'q' to quit.")
