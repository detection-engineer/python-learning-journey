# Objective: To create an interactive login log analyser that accepts user-provided login attempts, identifies unique IP addresses and detects failed login attempts.

# Initialising empty lists to store login attempts and unique IP addresses
total_attempts = []
ip_list = []

# Displaying instructions for entering login details
print ("\nLogin Details should be entered in the format IP - SUCCESS/FAILED or type 'q' to stop\n")

# Using a while loop to continuously accept login attempts
while True:
    attempts = input("\nEnter the login attempts details: ")

    # Using break to stop collecting input when the user enters 'q'
    if attempts == "q":
        break

    # Using append() to store each login attempt in the list
    total_attempts.append(attempts)

print ("\n-----------Summary of the Attempts: ----------\n", total_attempts)
print ("\n Total count of login attempts provided: ", len(total_attempts))

# Identifying unique IP addresses from the login attempts
print ("\nUnique IP address observed: \n")

for user_input in total_attempts:
        
    separate_list = user_input.split(" - ")

    if separate_list[0].strip() in ip_list:
        continue
    ip_list.append(separate_list[0].strip())

print ("Total Unique IP address: ", len(ip_list))
    
print ("\n", ip_list)

# Analysing failed login attempts
print ("\n-----------FAILED LOGIN SUMMARY----------\n")
failed_count = 0

# Using a for loop to iterate through all login records
for ipadd in total_attempts:
    ip_address = ipadd.split(" - ") 
    ip = ip_address[0].strip() 
    stats = ip_address[1].strip()

    # Skipping successful login attempts using continue
    if stats == "SUCCESS":
        continue

    # Displaying failed login attempts and increasing the failure counter
    print ("Login failure from: ", ip)
    failed_count +=1

# Displaying the total number of failed login attempts
print ("Total failed login attempts: ", failed_count)
