#!/usr/bin/env python3

import hashlib
import string
import socket
import time

def server_crack():

    # Open and read hashes.txt
    with open("hashes.txt", "r") as h:
        hashes = h.read().splitlines()

    # Open and read passwords.txt
    with open("passwords.txt", "r") as p:
        passwords = p.read().splitlines()

    # ASCII Lowercase letters
    characters = string.ascii_lowercase

    # Server information
    server_ip = "134.209.128.58"
    server_port = 1337

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))
    
    for i in range(0, 3):

        data = s.recv(1024)

        for c in characters:
            for p in passwords:
            
                # crack hashes
                val = c + p
                hashkey = hashlib.sha256(val).hexdigest()
            
                if hashkey in data:
                    print val,":",hashkey
                    s.send(val+"\n")

    # Obtain flag after 3 successful cracks
    data = s.recv(1024)
    print data
                    
if __name__ == "__main__":
    server_crack()
