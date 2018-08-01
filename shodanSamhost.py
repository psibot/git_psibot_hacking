#!/usr/bin/env python2
# Program: Ahodan Attack v1
# Author: psibot
# Purpose: Anything
# SCRIPT ONLY WORKS PYTHON V2
import shodan
import time
import os
from termcolor import colored, cprint
import sys
import socket
import paramiko
import threading
import shodan

SHODAN_API_KEY = "Your key"

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
  print "  \       \    Y    (  <_> ) /_/ | / __ \|   |  \ Host Hunter   |"
  print "/_______  /\___|_  / \____/\____ |(____  /___| /                |"
  print "      \/       \/             \/     \/     \/                  |"
  print "|   d3am0n711[@]gmail[dot]com                                   |"
  print "|   THIS will be only used for testing                          |"
  print "|---------------------------------------------------------------|\n"
  print W
logo()

API_KEY = "Your Key"
query = ' '.join(sys.argv[1:])
host = api.host(query)
print("""
        IP: {}
        Organization: {}
        Operating System: {}
""".format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))

# Print all banners
for item in host['data']:
        print("""
                Port: {}
                Banner: {}

        """.format(item['port'], item['data']))
