#!/usr/bin/env python

# define the server IP and port
HOST = "10.227.80.205"
PORT = 10000

# list of server ciphers available
SERVER_CIPHERS = ("CBC", "PCBC", "CFB", "RC4")

# list of ciphers available
CLIENT_CIPHERS = ("CBC", "PCBC", "CFB", "RC4")

# other variables
BUFSIZE = 1024

# state
OFFLINE = "off"
ONLINE = "on"
