#lets do this

login_attempts = [ "192.168.1.15 - FAILED",
    "192.168.1.15 - FAILED",
    "192.168.1.20 - SUCCESS",
    "192.168.1.15 - FAILED",
    "192.168.1.30 - FAILED",
    "192.168.1.30 - SUCCESS",
    "192.168.1.15 - FAILED",
    "192.168.1.40 - FAILED",
    "192.168.1.20 - FAILED"]

failed_count = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0

print ("\n----------Login summary------\n")

for attempts in login_attempts:
    ipadd = attempts.split(" - ")
    ip_address = ipadd[0].strip()
    status = ipadd[1].strip()

    print ("\nIP ADDRESS: ", ip_address, "Status: ", status, "\n")

print ("\n----------Failed Login summary------\n")


for stats in login_attempts:
    ipadd = stats.split(" - ")
    ip_address = ipadd[0].strip()
    status = ipadd[1].strip()
    if status == "SUCCESS":
        continue
    print ("\nAlert!!! FAILED login from IP address: ", ip_address, "\n")
    failed_count +=1

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

    if ip_address != "192.168.1.15":
        continue

print ("\nTOTAL FAILED LOGINS: ", failed_count, "\n")
print ("\n HIGH PRIORITY ALERT: SUSPICIOUS ACTIVITY DETECTED FROM IP ADDRESS: 192.168.1.15")

    