import socket
import subprocess
import time
from datetime import datetime


# Command to connect to a host or port
def port_scanner(host, port):
    s = socket.socket()
    try:
        s.connect((host, port))
    except:
        return False
    else:
        return True


# File for Results
myfile = open("Scaning Results", "w")


# User Input To be Displayed
host = input("Enter Ip Address: ")

MinRange = int(input('Starting Port Number:'))

MaxRange = int(input('Ending Port Number:'))

CheckRange = range(MinRange, MaxRange + 1, 1)


# Date and Time
now = datetime.now()

dt_string = now.strftime("%m/%d/%Y %H:%M:%S")

start = time.time()


# Host  Verification
status = subprocess.getstatusoutput("ping -n 1 " + host)

result = str(status)


# Results
if (result.startswith("(0")):
    print("Host is Responding, Start Port Scan.")
    print("Scan Starting at:", dt_string)

    #
    resp_tup = [host, "Responding, Started Scan at", dt_string, "\n"]

    resp_out = ' '.join(resp_tup)

    myfile.write(resp_out)
else:
    print("Host is not responding, Stop scan")
    resp_tup = [host, "Is Not Responding. Scan Stopped at", dt_string, "\n"]

    #
    resp_out = ' '.join(resp_tup)

    myfile.write(resp_out)

    myfile.close()
    exit()


# Stating Process
print("Scanning")


# Port Range
for i in CheckRange:
    if port_scanner(host, i):
        print("port", i, "is open")
        myfile.write("Port")
        myfile.write(str(i))
        myfile.write("is OPEN. \n")
    else:
        print("port", i, "is closed")
        check_tup = ["Port", str(i), "is CLOSED.", "\n"]
        resp_out = ' '.join(check_tup)
        myfile.write(resp_out)


# Processes Finished
end = time.time()
print("Task Completed. Port range", MinRange, "-", MaxRange, "has been scanned.")
elapsed = end - start
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Scan completed at:", dt_string)
print("Total scan time:", "%2f" % elapsed, "seconds.")
fin_tup = ["Scan ended at", str(dt_string), "\n"]
fin_out = ' '.join(fin_tup)
myfile.write(fin_out)
myfile.close()

# End of Assigment