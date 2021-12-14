# yara's first homework
# Yara's python homework
# https://www.notion.so/Yara-s-python-homework-d9a130181ab249649d8dbce8f5e46563
# 14.12.2021

# library to send requests to the internet and get the response
# put your code here:
from socket import *


# HOMEWORK:
# Variable for input from user (** ask for user name **)
# put your code here:
userName = input("what is the user name?\n")


# function to send a request to the internet and get our own hostname
# hostName = gethostname()
# put your code here:
hostName = gethostname()


# print the hostname that we got from function gethostname()

print(hostName)

# function to send a request to the internet and get our own IP address
# ipAddress = gethostbyname(hostName)
# put your code here:
ipAddress = gethostbyname(hostName)


# HOMEWORK:
# enter in the MISSING fields the two needed variables to print the IP address and the username
# print("The User: {} has the IP address".format(MISSING), MISSING)

# Solution 1 (easy, using f):
print("solution 1 using f:")
print(f"The user name is {userName}, and the ip address is {ipAddress}, and the host name is {hostName} ")

# Solution 2 (using .format() Method):
print("solution 2 using .format():")
print("The user name is {}, and the ip address is {}, and the host name is {}".format(userName,ipAddress, hostName))

# print the IP address that we got from function gethostbyname()
# *** This print() should be deleted once the homeowkr is done ***
# print(ipAddress)