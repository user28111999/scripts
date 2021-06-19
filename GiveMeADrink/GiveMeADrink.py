import telnetlib
import time
import sys

cmIP = '10.0.0.42:7001'
fdIP = '10.0.0.43'

con = telnetlib.Telnet(cmIP)

if sys.argv[1] == "coffee":
    con = telnetlib.Telnet(cmIP)
    con.write("sys brbrbr")
if sys.argv[1] == "redbull":
    con = telnetlib.Telnet(fdIP)
    time.sleep(21)
    con.write("sys opnopn")
    time.sleep(5) 
    con.write("sys closlc")