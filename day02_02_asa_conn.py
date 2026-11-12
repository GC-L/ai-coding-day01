import re
conn = 'TCP server  172.16.1.101:443 localserver  172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

result = re.match(r"(\S+)\s+server\s+(\S+):(\d+)\s+localserver\s+(\S+):(\d+)", conn)

print("{:<12}: {}".format("Protocol", result.group(1)))    
print("{:<12}: {}".format("Server IP", result.group(2)))
print("{:<12}: {}".format("Server Port", result.group(3)))
print("{:<12}: {}".format("Client IP", result.group(4)))
print("{:<12}: {}".format("Client Port", result.group(5)))