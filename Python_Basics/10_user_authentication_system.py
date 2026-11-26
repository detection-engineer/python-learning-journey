# Objective: To create a basic user authentication system that allows users to register and log in using a username and password.
# The program checks for duplicate usernames, validates user credentials, handles empty inputs, and provides an interactive menu for registration and login.

login_details = {}

# Function to register a new user and prevent duplicate usernames
def register(name, password):
    
        if name not in login_details:                   # Checking whether the username already exists
            login_details[name] = password
            print ("Registration completed!!")
        else:
            print ("\n Username Already exists")

# Function to authenticate users by verifying their username and password
def authentication (name, password):
        if name in login_details:
            if password == login_details[name]:        #Verifying the entered password against the stored password
                   print ("\n Welcome!!! You have been successfully authenticated")
            else:
                 print ("\n Incorrect Password!!! Please put correct credential")
        else:
            print ("\n Invalid Username!!! Please put correct credential")

# Function to collect and validate username and password inputs
def credentials():
    credentials_username = input ("\n Please enter the username: ")
    credentials_password = input ("\nPlease enter the password: ")

    # Checking for empty username or password inputs
    if credentials_username == "" or credentials_password == "":
         print("\n Username or Password cannot be empty")
         return None
    else: 
        return (credentials_username, credentials_password)

# Main program loop to display the menu and handle user selections
while True:

    # Handling invalid menu inputs to prevent program termination
    try:
        option = int ( input ("\nPlease select the option (1,2 OR 3): \n1. Register\n2. Login \n3. Quit \nInput: "))
        
        if option == 1:
            auth_credentials = credentials()
            if auth_credentials is None:
                continue
            username, password = auth_credentials
            register(username, password)

        elif option == 2:
            auth_credentials = credentials()
            if auth_credentials is None:
                continue
            username, password = auth_credentials
            authentication(username, password)

        elif option == 3:
           break
        else:
            print ("Invalid choice!! Try Again")

    except ValueError:
         print ("Invalid Option!! Try Again")

