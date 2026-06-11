def guess_number():
    import random

    number_to_guess = random.randint(1, 100)
    attempts = 0
    score = 0
    guessed_correctly = False
    print("Welcome to the guessing game! I'm thinking of a number between 1 and 100. Can you guess it?")

    while not guessed_correctly:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            if attempts >= 7:
                print("Game Over! You've used all your attempts. Better Luck Next Time!")
                break

            if user_guess < number_to_guess:
                print("too low! Try again.")
            elif user_guess > number_to_guess:
                print("too high! Try again.")
            else:
                guessed_correctly = True
                score = 100 - (attempts * 10)
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")
    

guess_number()


            