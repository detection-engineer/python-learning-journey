
# Yahooo!! I showed up!!
# Objective: To analyse a list of usernames and count how many login attempts were made by each user.

# Creating a list containing usernames from login attempts
user_names = ["admin", "john", "admin", "alice", "test", "john", "admin"]

# Initialising counters for each user
admin_count = 0
john_count = 0
alice_count = 0
test_count = 0

print ("-------- Login Attempts List ------------")

# Using a for loop to iterate through each username in the list
for name in user_names:
    print ("Login Attempt by:", name)      # Displaying the username for each login attempt

    # Checking which username made the login attempt
    if name == "admin":
        admin_count += 1
    elif name == "john":
        john_count += 1
    elif name == "alice":
        alice_count += 1
    elif name == "test":
        test_count += 1

# Displaying the count summary of login attempts
print ("----------- Login Attempt Count Summary ---------")

print ("Admin login attempt count:", admin_count)
print ("John login attempt count:", john_count)
print ("Alice login attempt count:", alice_count)
print ("Test user login attempt count:", test_count)
print("Total login attempts:", len(user_names))