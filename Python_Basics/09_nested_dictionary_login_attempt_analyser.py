# Objective: To create an interactive login attempt analyser using nested dictionaries to track successful and failed login attempts for each IP address.
# The program validates user input, maintains per-IP login statistics, detects suspicious login activity, and identifies known malicious IPs, including successful logins from those IPs.

print("\n------------ LOGIN ATTEMPT ANALYSER ------------\n")

print ("Enter IP address and status (SUCCESS/FAILED)")
print("Type 'q' to quit.\n")

# Initialise an empty dictionary to store IP addresses and login statuses
login_attempts = {}

# Storing a set of known malicious IP addresses for detection
malicious_ip = {"102.23.49.9", "203.12.13.2", "45.10.23.45", "78.23.67.109"}

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
    
print ("\n------------ IP SUMMARY ------------")
print ("IPs Observed")
for ipadd in login_attempts.keys():
    print( "\n" + f"- {ipadd}")

# Initialising counters for overall login statistics
total_attempts = 0
fail_count = 0 
success_count = 0

# Initialising counters to track login attempts from known malicious IPs
malicious_ip_count = 0
malicious_count_success = 0
malicious_count_failed = 0

print ("\n------------ SUSPICIOUS LOGIN SUMMARY ------------")

# Iterating through each IP address and its login statistics
for key, value in login_attempts.items():

    # Displaying the failed login count for each IP
    print (f"\n Failed login summary: {key} - {value["FAILED"]}")

     # Generating an alert if an IP has more than 3 failed login attempts
    
    if value["FAILED"] >3:
      print (f"Alert!!! Suspicious number of login attempts from {key} ")

    # Checking whether the observed IP is present in the known malicious IP set
    if key in malicious_ip:
        print ("\nHIGH PRIORITY ALERT: ")
        print (f"\nLogin attempt observed from {key} which is a malicious IP")

        malicious_ip_count +=1
        malicious_count_failed += value["FAILED"]
        malicious_count_success += value["SUCCESS"]

        # Generating a critical alert if a known malicious IP has successful logins
        if value["SUCCESS"]:
            print ("\n CRITICAL ALERT: ")
            print (f"\nSuccessful Login: {value['SUCCESS']} from known malicious IP {key}")

    

    # Calculating total, failed and successful login attempts
    total_attempts += sum(value.values())
    fail_count +=  value["FAILED"]
    success_count += value["SUCCESS"]

# Displaying the overall login statistics

print ("\n------------ TOTAL LOGIN SUMMARY ------------")
print (f"\nTotal login attempts: {total_attempts} ")
print (f"\nTotal Success attempts: {success_count}")
print (f"\n Total Failed attempts: {fail_count}")

print ("\n------------ MALICIOUS IP LOGIN ATTEMPTS SUMMARY ------------")
print (f"\n Unique malicious IPs observed: {malicious_ip_count}")
print (f"\n Total failed attempts from malicious IPs: {malicious_count_failed}")
print (f"\n Total successful attempts from malicious IPs: {malicious_count_success}")

print ("\n------------ END OF PROGRAM ------------\n")