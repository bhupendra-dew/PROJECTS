import random
import math

# Initializing the game
def game():

    # Taking Inputs
    lower_bound = int(input("Enter Lower bound :- "))
    upper_bound = int(input("Enter Upper bound :- "))

    # generating a random number between the lower and upper bound
    chances = 0
    random_number = random.randint(lower_bound, upper_bound)
    chances = round(math.log(upper_bound - lower_bound + 1, 2))
    print("\n\tYou've only ", chances, " chances to guess the integer!\n")

    # Initializing the number of guesses.

    guess_count = 0

    while guess_count < math.log(upper_bound - lower_bound + 1, 2):
        guess_count += 1
        if guess_count < chances:
                print("You still have ", (chances + 1) - guess_count, " chances to guess the number")
        elif guess_count == chances:
            print("This is your last chance!")
        else:
            print("Your chances are over!")
        # Taking guessing number as input

        guess = int(input("Guess a number :- "))

        if random_number == guess:
            print("Congratulations you did it in ", guess_count, " try")
            print("Want to play again? (yes/no)")
            ans = input("Yes/No :- ")
            if ans == "Yes" or ans == "yes":
                game()
            elif ans == "No" or ans == "no":
                print("Thanks for playing!")
                break
            else:
                print("Invalid Input")
                break 

        elif random_number > guess:
            print("You guessed too small!")
            print("Try Again")

        else:
            print("You Guessed too high!")
            print("Try Again")

        # If Guessing is more than required guesses
        if guess_count >= math.log(upper_bound - lower_bound + 1, 2):
            print("\nThe number is %d" % random_number)
            print("\tBetter Luck Next time!")
            break

# Driver Code
if __name__ == "__main__":
    # Calling the game function
    game()