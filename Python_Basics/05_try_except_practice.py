# Welcome to the Guessing Game!!! Let's see if you can guess the number I have in mind. 
# You have 3 attempts to guess the correct number. Good Luck!!!


# Setting the player’s maximum attempts to 3
attempts = 3

# Using a while loop to allow the player to guess the number until they run out of attempts
while attempts > 0:

    # Using a try-except block to handle invalid input from the player
    try:
        number = int(input("Guess the number: "))

        # Checking if the guessed number is correct
        if number == 25:
            print ("\n You guessed it right!!! \n")
            break

        else:
            print ("\n Wrong guess!!! \n")
            attempts -=1                # decreasing the number of attempts by 1
            print (attempts, "attempts remaining")

    except ValueError:
        print("Ahhaa!!! That's not a valid number. You have lost an attempt. Try again!!!")
        attempts -=1
        print (attempts, "attempts remaining")

# Checking if the player has exhausted all their attempts
if attempts == 0:
    print ("\n GAME OVER!!! You have exhausted all your attempts. \n")
