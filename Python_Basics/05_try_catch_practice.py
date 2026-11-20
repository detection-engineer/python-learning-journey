# Let's test

attempts = 3

while attempts > 0:
    try:
        number = int(input("Guess the number: "))
        if number == 25:
            print ("\n You guessed it right!!! \n")
            break
        else:
            print ("\n Wrong guess!!! \n")
            attempts -=1
            print (attempts, "attempts remaining")
    except ValueError:
        print("Number!!!! You need to guess the number")
        attempts -=1
        print (attempts, "attempts remaining")

if attempts == 0:
    print ("\n GAME OVER!!! You have exhausted all your attempts. \n")
