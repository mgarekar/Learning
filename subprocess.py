# Basic Subprocess module
# Input = python DOMAIN
# OUTPUT = SUCCESSFUL or ERROR
# Processing = check if system can reach domain

import subprocess # TO RUN COMMANDS ON lINUX
import sys # TO GIVE INPUT TO PYTHON PROGRAMS

if len(sys.argv) !=2:
    print "Error, Enter the domain name you want to ping"
    sys.exit()

DOMAIN_TO_PING=sys.argv[1]
output_code=subprocess.call(["ping",str(DOMAIN_TO_PING),"-c","1","-q","-w","1"])

if output_code==0:
    print "successful"
else:
    print "error"
    sys.exit()
