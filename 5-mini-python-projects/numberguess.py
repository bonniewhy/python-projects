# 2. GUESS THE NUMBER ---
#       TODO: Similar to the first project, this project also uses the random module in
#       Python. The program will first randomly generate a number unknown to the user.
#       The user needs to guess what that number is. (In other words, the user needs to
#       be able to input information.) If the user's guess is wrong, the program should
#       return some sort of indication as to how wrong (e.g. The number is too high or
#       too low). If the user guesses correctly, a positive indication should appear.
#       You'll need functions to check if the user input is an actual number, to see the
#       difference between the inputted number and the randomly generated numbers, and to
#       then compare the numbers.
#
#       Concepts to keep in mind:
#           -- Random function
#           -- Variables
#           -- Integers
#           -- Input/Output
#           -- Print
#           -- While loops
#           -- If/Else statements
#
#       Jumping off the first project, this project continues to build up the base knowledge
#       and introduces user-inputted data at its very simplest. With user input, we start to
#       to get into a little bit of variability.
import random
import time

def main():
    player_name = input("Hello! What is your name? ")
    
    # Give the computer a few seconds to "think" and make a response.
    time.sleep(0.5)
    print("Nice to meet you," + player_name + "!")

    computer_number = random.randint(1, 20)
    # The computer is "thinking" of a number.
    time.sleep(2)
    print("I'm thinking of a number between 1 and 20.")
    time.sleep(0.5)
    print("You have seven tries to guess.")

    num = 0

    while num < 7:
        time.sleep(1)
        number_guess = int(input("What do you think it is? "))
        if number_guess > computer_number:
            print("Too high! Try again, please!")
            num += 1
        elif number_guess < computer_number:
            print("Too low! Try again, please!")
            num += 1
        else:
            print("Good Guess! You win!")
            break

if __name__ == "__main__":
    main()