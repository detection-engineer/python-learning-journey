# Objective: To create an interactive login log analyser using Python dictionaries to store IP addresses and login statuses.
# The program validates user input and counts successful and failed login attempts.

# Display program instructions
print("\n--------------- LOGIN ATTEMPT ANALYSER ---------------\n")
print ("Format: IP - SUCCESS/LOGIN")
print("Type 'q' to quit.\n")

# Initialise an empty dictionary to store IP addresses and login statuses
login_attempts = {}

# Accepting IP addresses and login statuses from the user
while True:

    key = input ("\nPlease enter the IP address:  ")

    # Exit the loop when the user enters 'q'
    if key == "q":
        break

    # Asking the user to enter the login status for the given IP
    value = input (f"Enter login status for {key} (SUCCESS/FAILED): ")

    # Validating the login status before storing it
    if value == "SUCCESS" or value == "FAILED":
        login_attempts [key] = value
    else:
        print ("Invalid status! Please enter SUCCESS or FAILED.\n")

# Displaying all collected login details
print("\n---------------LOGIN RECORD SUMMARY---------------\n")

print (login_attempts)
print ("\nTotal entry found: \n", len(login_attempts))

print("\nIP Addresses Observed:")
for ip in login_attempts.keys():
    print(f"- {ip}")

# Initialising counters for successful and failed logins
success_count = 0
failure_count = 0


print ("\n---------------Login failure summary---------------\n")

# Iterating through the dictionary and analyse login statuses
for ip, stats in login_attempts.items():

    # Counting successful logins and skip failure reporting
    if stats == "SUCCESS":
        success_count +=1
        continue

    # Display failed login records
    print (f"\n {ip} - has {stats} attempts")
    failure_count +=1

# Display the final login statistics

print("\n---------------FINAL LOGIN STATISTICS---------------\n")
print (f"\nTotal Successful Logins: {success_count}")
print (f"\nTotal Failed Logins: {failure_count}")
print(f"\nTotal Logins: {len(login_attempts)}")


print("\n---------------ANALYSIS COMPLETED---------------\n")