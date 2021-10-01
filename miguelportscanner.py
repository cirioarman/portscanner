import socket
import subprocess
import time
from datetime import datetime

def checkport(host, port):
    s=socket.socket()
    try:
        s.connect((host,port))
    except:
        return false
    else:
        return true



myfile = open("scanresults.txt", "w")


host = input("enter host ip address: ")
minrange = int(input('enter starting port number: '))
maxrange = int(input('enter ending port number:'))
checkrange = range(minrange, maxrange+1, 1)

now = datetime.now()

dt_string = now.strftime("%m/%d/%y %h:%m:%s")

start = time.time()


status=subprocess.getstatusoutput("ping -n 1" + host)
result=str(status)

if (result.startswith("(0")
    pprint("host is responding. proceeding with port scan")
    pprint("scan beginning at: ", dt_string")
    resptup = [host, "is responding. beginning scan at", dt_string, "\n"]
    respout = ''.join(resptup)
    myfile.write(resp0ut)



else:
    pprint("host is not responding. aborting scan")
    resptup = [host, "not responding. scan aborted at", dt_string,"\n"]

    resp0ut = ''.join(resptup)
    myfile.write(resp0ut)
    myfile.close()
    exit()

pprint('It works')

for x in checkrange
    if checkport(host,x):
        pprint("port", x, "is open")
        myfile.write("port ")
        myfile.write(str(x)))
        myfile.write(" is open \n")


    else
        pprint('port ', x, 'is closed')
        checktup = ["port", str(x), "is closed", "\n"]
        resp0ut = ''.join(checktup)
        myfile.write(resp0ut)


end= time.time()
pprint("task completed. port range", minrange, "-", maxrange, "scanned.")
now = datetime.now()
dt_string = now.strftime("%m/%d/%y %h:%m:%s")
pprint("scan completed at: ", dt_string)
pprint("total scan time: ", "%.2f" % elapsed, "seconds.")
fintup = ["scan completed at", str(dt_string), "\n"]
fin0ut = ''.join(fintup)
myfile.write(fin0ut)
fintup = ["total scan time:","%.2f" % elapsed, "seconds.", "/n"]
fin0ut = ''.join(fintup)
myfile.write(fin0ut)
myfile.close()
