#!/usr/bin/env python2
# Program: SSH Dictionary Attack v1
# Author: psibot
# Purpose: Brutforce SSH !!!
# SCRIPT ONLY WORKS PYTHON V2
import nmap
import time
import os
from termcolor import colored, cprint
import sys
import socket
import paramiko
import threading
import shodan

SHODAN_API_KEY = "Your Shodan Key"

api = shodan.Shodan(SHODAN_API_KEY)


# Colours
W  = "\033[0m";
R  = "\033[31m";

# Banner
def logo():
  os.system('clear')
  cprint('--------------------------------------------------------------', 'green',attrs=['bold'])
  print colored('[+]', 'red'), colored('Shodan V1', 'red')
  print colored('[+]', 'red'), colored('....Find anything!.....', 'green')
  cprint('--------------------------------------------------------------', 'green',attrs=['bold'])
  print R+"\n|---------------------------------------------------------------|"
  print "  _________ ___ ___            .___                             |"
  print " /   _____//   |   \  ____   __| _/____    ____                 |"
  print " \_____  \/    ~    \/  _ \ / __ |\__  \  /    \                |"
  print "  \       \    Y    (  <_> ) /_/ | / __ \|   |  \               |"
  print "/_______  /\___|_  / \____/\____ |(____  /___| /                |"
  print "      \/       \/             \/     \/     \/                  |"
  print "|   d3am0n711[@]gmail[dot]com                                   |"
  print "|   THIS will be only used for testing                          |"
  print "|---------------------------------------------------------------|\n"
  print W
logo()

API_KEY = "Your Shodan Key"
if len(sys.argv) == 1:
        print 'Usage: %s <search query>' % sys.argv[0]
        sys.exit(1)

try:
        # Setup the api
        api = shodan.Shodan(API_KEY)

        # Perform the search
        nm = nmap.PortScanner()
        query = ' '.join(sys.argv[1:])
        result = api.search(query)

        # Loop through the matches and print each IP
        for service in result['matches']:
            print service['ip_str']
            nm.scan(service['ip_str'],'22')
            nm.command_line()
            nm.scaninfo()

except Exception as e:
        print 'Error: %s' % e


        sys.exit(1)
