#!/usr/bin/env python2

import sys
import struct
from datetime import datetime
import re

# You can use this method to exit on failure conditions.
def bork(msg):
        sys.exit(msg)

png_count = 0 
gif_count = 0
# Some constants. You shouldn't need to change these.
MAGIC = 0x8BADF00D
VERSION = 1

if len(sys.argv) < 2:
        sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
        data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8

offset = 0


magic, version= struct.unpack("<LL", data[offset:offset+8])

if magic != MAGIC:
        bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
        bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))

offset += 8
t_stamp, _ = struct.unpack("<LL", data[offset:offset+8])
time = int(t_stamp)
print("TimeStamp: " + datetime.utcfromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S'))
offset += 4
author = struct.unpack("8s", data[offset:offset+8])
print("Author: '{0}'".format(author[0].decode("utf-8")))
offset += 4
_,sec_count = struct.unpack("<LL", data[offset:offset+8])
print("Section Count: %d" % int(sec_count))
# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")
offset += 8
slen = 1
section_num = 1
to_print = ""
for x in range(sec_count) :
        stype, slen = struct.unpack("<LL", data[offset:(offset+8)])
        print("___________________________")
        print("SECTION TYPE: %s" % hex(stype))
        print("SECTION LENGTH: %d" % int(slen))
        offset = offset + 8
        print(" length: %d" %(slen))
        if (stype == 1):
            print("Section: ASCII")
            message, = struct.unpack("<%ds" % slen, data[offset:offset+slen])
            offset = offset + slen
            print("Message: %s" % message)
        
        elif (stype == 2):
            print("Section: Words")
            message = struct.unpack("<%dq" % temp, data[offset:offset+slen])
            offset = offset + slen
            print("Message: %s" % message.encode('utf-8'))
        
        elif (stype == 3):
            print("Section: Words")
            temp = slen/8
            message = struct.unpack("<%dq" % temp, data[offset:offset+slen])
            offset = offset + slen
            print("Message: %s" % message)
        elif (stype == 4):
            for i in range(int(slen)/8):
                s = struct.unpack("S", data[offset:offset+8])
            offset += 8
        elif (stype == 5):
             print("Section: DOUBLES")
             for a in range(0, slen, 8):
                message, = struct.unpack("<d", data[offset+a:offset+a+8])
                print("Message: %d" % message)
        elif (stype == 6):
                print("Section: COORD")
                lat,lon = struct.unpack("dd",data[offset:offset+16])
                offset += 16
                print("COORD :  (%f,%f)" % (lat,lon))

        elif (stype == 7):
            print("Section: REFERENCE")
            ref, = struct.unpack("<L", data[offset:(offset+slen)])
            print("Message: %d" % ref)
            offset = offset + slen


        elif (stype  == 8):
                png_count += 1
                tmp_str = str(png_count) + ".png"
                with open(tmp_str,  "wb") as f:
                        f.write(bytes([137,80,78,71,13,10,26,10]))
                        l = struct.unpack(str(slen)+"s",data[offset:offset + slen])
                        f.write(l[0])
                offset += int(slen)
print("----------------- DONE PARSING ---------------")
     
         