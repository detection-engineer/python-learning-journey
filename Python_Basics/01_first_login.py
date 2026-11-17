
# First program.. Yay!!
# Basic Username and Password Validation
# Concepts: Variables, User Input and If/Else Statements

# VERSION 1: Using Nested If/Else Statements

user_name = "admin"             #hardcoded username
user_pass = "Test@123"          #hardcoded password

login_id = input("Please enter your username: ")       #accepting username from user
login_pass = input("Please enter your password: ")     #accepting password from user

if user_name == login_id:                   #checking if username is correct
    if user_pass == login_pass:             #checking if password is correct
        print("Access Granted!!!")
    else:
        print("Invalid Password")
else:
    print("Invalid Username")




# VERSION 2: Using the AND Operator

user_name = "admin"             #hardcoded username
user_pass = "Test@123"          #hardcoded password

login_id = input("Please enter your username: ")       #accepting username from user
login_pass = input("Please enter your password: ")     #accepting password from user

if user_name == login_id and user_pass == login_pass:   #checking if username and password are correct
    print("Access Granted!!!")
else:
    print("Invalid Username or Password")