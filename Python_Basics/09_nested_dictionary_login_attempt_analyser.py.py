# Objective: To create an interactive login attempt analyser using nested dictionaries to track successful and failed login attempts for each IP address.
# The program validates user input, maintains per-IP login statistics, and flags IP addresses with more than 3 failed login attempts.

print("\n--------------- LOGIN ATTEMPT ANALYSER ---------------\n")
print ("Enter IP address and status (SUCCESS/FAILED)")
print("Type 'q' to quit.\n")

# Initialise an empty dictionary to store IP addresses and login statuses
login_attempts = {}

# Accepting IP addresses and login statuses from the user
while True:

    ip = input ("\nPlease enter the IP address:  ")

    # Exit the loop when the user enters 'q'
    if ip == "q":
        break

    # Asking the user to enter the login status for the given IP
    attempt = input (f"Enter login status for {ip} (SUCCESS/FAILED): ")

    # Validating the login status entered by the use
    if attempt == "SUCCESS" or attempt == "FAILED":
        if ip not in login_attempts:
                login_attempts [ip] = {"SUCCESS" : 0,
                                       "FAILED" : 0}
    else: 
        print ("Invalid status! Please enter SUCCESS or FAILED.\n")
        continue

    # Incrementing the relevant login status count for the IP address
    login_attempts [ip][attempt] +=1
    
print ("\n------------IP Summary--------------")
print ("IPs Observed")
for ipadd in login_attempts.keys():
    print( "\n" + f"- {ipadd}")

# Initialising counters for overall login statistics
total_attempts = 0
fail_count = 0 
success_count = 0

print ("\n------------Failed Login Summary------------")

# Iterating through each IP address and its login statistics
for key, value in login_attempts.items():

    # Displaying the failed login count for each IP
    print (f"\n {key} - {value["FAILED"]}")

     # Generating an alert if an IP has more than 3 failed login attempts
    if value["FAILED"] >3:
      print (f"Alert!!! Suspicious number of login attempts from {key} ")

    # Calculating total, failed and successful login attempts
    total_attempts += sum(value.values())
    fail_count +=  value["FAILED"]
    success_count += value["SUCCESS"]

# Displaying the overall login statistics

print ("\n----------------Total Login Summary------------")
print (f"\nTotal login attempts: {total_attempts} ")
print (f"\nTotal Success attempts: {success_count}")
print (f"\n Total Failed attempts: {fail_count}")

print ("\n-----End Of Program----------\n")