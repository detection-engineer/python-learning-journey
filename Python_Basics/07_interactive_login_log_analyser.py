total_attempts = []
ip_list = []

print ("\nLogin Details should be entered in the format IP - SUCCESS/FAILED or type 'q' to stop\n")


while True:
    attempts = input("\nEnter the login attempts details: ")
    if attempts == "q":
        break

    total_attempts.append(attempts)

print ("\n-----------Summary of the Attempts: ----------\n", total_attempts)
print ("\n Total count of login attempts provided: ", len(total_attempts))

print ("\nUnique IP address observed: \n")

for user_input in total_attempts:
        
    separate_list = user_input.split(" - ")

    if separate_list[0].strip() in ip_list:
        continue
    ip_list.append(separate_list[0])

print ("Total Unique IP address: ", len(ip_list))
    
print ("\n", ip_list)

print ("\n-----------FAILED LOGIN SUMMARY----------\n")
failed_count = 0

for ipadd in total_attempts:
    ip_address = ipadd.split(" - ")
    ip = ip_address[0].strip() 
    stats = ip_address[1].strip()

    if stats == "SUCCESS":
        continue
    
    print ("Login failure from: ", ip)
    failed_count +=1

print ("Total failed login attempts: ", failed_count)
