#!/bin/python3

import sys #allow to enter command line arguments
import socket
from datetime import datetime

#define target
if len(sys.argv) ==2: #walidacja. argumenty muszą byc 2. arg0 to nazwa skryptu. arg1 to ip. muszą być oba
    target = socket.gethostbyname(sys.argv[1]) #translates hostname to ipv4
else:
    print("Invalid amount of arguments.")
    print("Sytax: python3 scanner.py <ip>")
    sys.exit() #wychodzi zprogramu. jest tego nie ma to sie zwiesi

#add banner
print("-"*50)
print("Scanning target"+ target)
print("Time started:"+ str(datetime.now()))
print("-"*50)

try: #probujemy cos, jesli bedzie jakis exception to zamkniemy program
    for port in range(50,85):
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET to ipv4, SOCK_STREAM to port
        socket.setdefaulttimeout(1) #to jest float, można dać coś z przecinkiem
        result= s.connect_ex((taget.port)) #zwraca error indicator. jesli nie ma erroru to zwórci 0

        print("Checking port {}.".format(port))

        if result == 0:
            print("Port {} is open.".format(port))
            s.close()
except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Couldn't connect to server.")
    sys.exit()