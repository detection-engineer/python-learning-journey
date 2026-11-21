# Objective: To analyse login attempts, identify failed logins, count failed attempts from different IP addresses.
# Generate a high-priority alert for suspicious activity.

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

# Initialising counters
failed_count = 0

# Initialising individual counters for each IP address
count1= 0
count2 = 0
count3 = 0
count4 = 0

# Displaying a summary of all login attempts
print ("\n----------Login summary------\n")

# Using a for loop to iterate through each login attempt
for attempts in login_attempts:

    # Using split() to separate the IP address and login status
    ipadd = attempts.split(" - ")

    # Using strip() to remove any unnecessary whitespace
    ip_address = ipadd[0].strip()
    status = ipadd[1].strip()

    print ("\nIP ADDRESS: ", ip_address, "Status: ", status, "\n")

# Displaying failed login attempts
print ("\n----------Failed Login summary------\n")

# Using a second for loop to analyse login attempts
for stats in login_attempts:
    ipadd = stats.split(" - ")
    ip_address = ipadd[0].strip()
    status = ipadd[1].strip()

    # Skipping successful login attempts using continue
    if status == "SUCCESS":
        continue
    print ("\nAlert!!! FAILED login from IP address: ", ip_address, "\n")
    failed_count +=1            # Initialising the total number of failed login attempts counter

    # Counting failed login attempts for each individual IP address
    if ip_address == "192.168.1.15":
        count1 += 1
        print (count1, "failed login attempts from 192.168.1.15")
    if ip_address == "192.168.1.20":
        count2 += 1
        print (count2, "failed login attempts from 192.168.1.20")
    if ip_address == "192.168.1.30":
        count3 += 1
        print (count3, "failed login attempts from 192.168.1.30")
    if ip_address == "192.168.1.40":
        count4 += 1
        print (count4, "failed login attempts from 192.168.1.40")

    # Skipping other IP addresses using continue
    # Focusing on failed login attempts from 192.168.1.15
    if ip_address != "192.168.1.15":
        continue

print ("\nTOTAL FAILED LOGINS: ", failed_count, "\n")

# Checking whether the target IP has exceeded the failure threshold
if count1 > 3:
    print ("\n HIGH PRIORITY ALERT: SUSPICIOUS ACTIVITY DETECTED FROM IP ADDRESS: 192.168.1.15")        # Generating a high-priority alert if more than 3 failed attempts are detected