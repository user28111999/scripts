import telnetlib
papaIP = "10.0.0.4"
con = telnetlib.Telnet(papaIP)
con.write("displayswitch.exe/clone")