#!/usr/bin/env python

# Basic starter Script
################################################################
#
# You will need pwntools installed
#       https://github.com/Gallopsled/pwntools
# On most systems
#       pip install pwntools 
#
# Usage:
#		python template.py [RHOST=] [RPORT=]
#
# test it locally with nc -l 4444
################################################################


# Imports
################################################################
from pwn import *
#from sympy import *       #for math stuffz
	#solve(Eq(x+8,2))
#from ctypes import *
#import string



# Global vars
################################################################
host 		= args['RHOST'] or "localhost"   # passed as arguments or hardcode
port 		= args['RPORT'] or "4444"        # passed as arguments or hardcode
user 		= args['USER']  or ''
password 	= args['PASS']  or ''
binary		= args['BIN']   or './path/to/binary'
#context(arch='i386',os='linux')      # set a global context for asm/disasm




# Initial Connection
################################################################################################
# Set up connection and get first response
# pwntools takes care of our socket setup and teardown
#
# .sendline() and .recvline() use \n as a delim to end the send/recieve
# .recv() and .recvall() are also available
# Send and recv just take what is thrown back @ a default size of 4096, 
# interactive() basically switches you into a session like you nc'd to the server


conn = remote(host, port)
#resp = conn.interactive()               #if you want to manually try things out first

resp = conn.recvline()
print "Server sent:   " + resp
resp = conn.recvline()                   #Sometimes initial connects send us 2 lines   
print "Server sent:  " + resp

#data2send = "some send stuff"
#print "Sending: " + data2send
#conn.sendline(data2send)

#resp = conn.recvline()
#print "response wuz: " + resp




# Solve that shit here
################################################################################################

data2send = "some data and stuff"
print "Sending: " + data2send
conn.sendline(data2send)

resp = conn.recvline()
print "Server sent: " + resp   #final response   the FLAG!!! 


# Shut it down
################################################################################################


conn.close() #close connection














################################################################################################
################################################################################################
#	Solutions! 
#
#   trying this out, to keep solutions to challs as comments in a big ol script
#	might be better to pull out into its own
################################################################################################
################################################################################################

#solve equations for internetwache
'''
while True:

	data2 = s.recv(size)
	print "The eq: " + data2
	strr = data2.split(':')
	x = Symbol('x')
	y = Symbol('y')
	equation = strr[1].rstrip()  # ' x +1 = 9'
	eq = equation.split('=')
	left = eq[0]
	right = eq[1]
	an = solve(Eq(sympify(left), sympify(right)))
	s.send(str(an[0]))
	data2 = s.recv(size)
	print "is it right? " + data2

s.close()
'''
################################################################################################


################################################################################################


################################################################################################


################################################################################################


################################################################################################


################################################################################################


################################################################################################


################################################################################################


################################################################################################


################################################################################################


################################################################################################


################################################################################################


################################################################################################






























