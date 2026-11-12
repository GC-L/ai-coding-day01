import re
mac_table = '166    54a2.74f7.0326    DYNAMIC     Gi1/0/11'
result = re.match(r"(\d+)\s+(\w+\.\w+\.\w+)\s+(\w+)\s+(\S+)", mac_table)


print("{:<6}: {}".format("VLAN", result.group(1)))    # 得到 "VLAN  : 166"
print("{:<6}: {}".format("MAC", result.group(2)))    # 得到 "MAC   : 54a2.74f7.0326"
print("{:<6}: {}".format("Type", result.group(3)))    # 得到 "Type  : DYNAMIC"
print("{:<6}: {}".format("Port", result.group(4)))    # 得到 "Port : Gi1/0/11"