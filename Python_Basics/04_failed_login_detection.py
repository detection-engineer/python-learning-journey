# Objective: To analyse login attempts, count successful and failed logins and identify IP addresses with multiple failed login attempts.

# Creating a list containing IP addresses and their login status
login_attempts = [ "192.168.1.15 - FAILED",
    "192.168.1.15 - FAILED",
    "192.168.1.20 - SUCCESS",
    "192.168.1.15 - FAILED",
    "192.168.1.30 - FAILED",
    "192.168.1.30 - SUCCESS",
    "192.168.1.15 - FAILED",
    "192.168.1.40 - FAILED",
    "192.168.1.20 - FAILED"]

# Initialising counters to track login attempts for each IP address
ip_count1 = 0
ip_status_success1 = 0
ip_status_failure1 = 0

ip_count2 = 0
ip_status_success2 = 0
ip_status_failure2 = 0

ip_count3 = 0
ip_status_success3 = 0
ip_status_failure3 = 0

ip_count4 = 0
ip_status_success4 = 0
ip_status_failure4 = 0

# Initialising counters to track total successful and failed logins
success_stat = 0
failure_stat = 0

# Using a for loop to iterate through each login attempt
for attempts in login_attempts:
    
    # Splitting the login attempt to extract the IP address and login status
    ipadd = attempts.split("-")
    ip_address = ipadd[0].strip()
    login_status = ipadd[1].strip()

    # Counting total successful and failed login attempts
    if login_status == "FAILED":
        failure_stat += 1
    else:
        success_stat += 1

    # Checking the IP address and counting its total login attempts
    if ip_address == "192.168.1.15":
        ip_count1 += 1

        # Counting successful and failed login attempts for this IP
        if login_status == "FAILED":
            ip_status_failure1 += 1
        else:
            ip_status_success1 += 1

    elif ip_address == "192.168.1.20":
        ip_count2 += 1

        # Counting successful and failed login attempts for this IP
        if login_status == "FAILED":
            ip_status_failure2 += 1
        else:
            ip_status_success2 += 1

    elif ip_address == "192.168.1.30":
        ip_count3 += 1

        # Counting successful and failed login attempts for this IP
        if login_status == "FAILED":
            ip_status_failure3 += 1
        else:
            ip_status_success3 += 1

    elif ip_address == "192.168.1.40":
        ip_count4 += 1

        # Counting successful and failed login attempts for this IP
        if login_status == "FAILED":
            ip_status_failure4 += 1
        else:
            ip_status_success4 += 1

# Displaying the overall login attempt summary
print ("\nLogin Attempt Summary:\n")
print ("Total login attempts: ", len(login_attempts))
print ("Successful logins: ", success_stat)
print ("Failed logins: ", failure_stat)

# Displaying login activity for each IP address
print ("\n IP Address: 192.168.1.15")
print ("Total attempts: ", ip_count1)
print ("Successful logins: ", ip_status_success1)
print ("Failed logins: ", ip_status_failure1)
print (" \nIP Address: 192.168.1.20")
print ("Total attempts: ", ip_count2)
print ("Successful logins: ", ip_status_success2)
print ("Failed logins: ", ip_status_failure2)
print (" \nIP Address: 192.168.1.30")
print ("Total attempts: ", ip_count3)
print ("Successful logins: ", ip_status_success3)
print ("Failed logins: ", ip_status_failure3)
print ("\nIP Address: 192.168.1.40")
print ("Total attempts: ", ip_count4)
print ("Successful logins: ", ip_status_success4)
print ("Failed logins: ", ip_status_failure4)

# Identifying IP addresses with 3 or more failed login attempts
if ip_status_failure1 >= 3:
    print ("\nALERT: Multiple failed login attempts detected from IP Address: " + "192.168.1.15 \n")
if ip_status_failure2 >= 3:
    print ("\nALERT: Multiple failed login attempts detected from IP Address: " + "192.168.1.20 \n")
if ip_status_failure3 >= 3:
    print ("\nALERT: Multiple failed login attempts detected from IP Address: " + "192.168.1.30 \n")
if ip_status_failure4 >= 3:
    print ("\nALERT: Multiple failed login attempts detected from IP Address: " + "192.168.1.40 \n")
