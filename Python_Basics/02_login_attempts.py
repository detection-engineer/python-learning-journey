# Yay Again!! Second one.. 
# Using Nested If/Else Statements with a limit on login attempts


#Version 1: Checking username and password together and giving the user 4 attempts to enter the correct username and password


user_name = "admin"                         # hardcoded username
user_pass = "Test@123"                      # hardcoded password

attempt_count = 4                                                         # setting the number of attempts to 4

while attempt_count > 0:                          # looping until the number of attempts is greater than 0
    login_id = input("Please enter your username: ")            # accepting username from user
    login_pass = input("Please enter your password: ")          # accepting password from user

    if user_name == login_id and user_pass == login_pass:       # checking if username and password are correct
        print (" \n Access Granted!!! \n")
        break
    else:
        print ("Invalid Username or Password")
        attempt_count = attempt_count - 1                       # decreasing the number of attempts by 1
        print (attempt_count, "attempts remaining")             # accepting username and password from user again

if attempt_count == 0:
    print ("\n STOP!!!Too many attempts!!! \n")




# Version 2: Checking username and password separately and giving the user 4 attempts to enter the correct username and password

user_name = "admin"                         # hardcoded username
user_pass = "Test@123"                      # hardcoded password
attempt_count = 3                           # setting the number of attempts to 4

while attempt_count>0:                                          # looping until the number of attempts is greater than 0
    login_id = input("Please enter your username: ")            # accepting username from user
    login_pass = input("Please enter your password: ")          # accepting password from user

    if user_name == login_id:                               # checking if username is correct
        if user_pass == login_pass:                         # checking if password is correct
            print (" \n Access Granted!!! \n")
            break
        else:
            print ("Invalid Password") # accepting username and password from user again
    else:
        print("Invalid Username")  # accepting username and password from user again

    attempt_count = attempt_count - 1                                              # decreasing the number of username attempts by 1

if attempt_count == 0:
    print ("\n STOP!!!Too many attempts!!! \n")