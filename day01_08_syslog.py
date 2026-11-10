import re

date = "2026-03-03"
hostname = "SW-Core-01"
level = "CRITICAL"
message = "%LINK-3-UPDOWN: Interface GigabitEthernet0/2, changed state to up"
result = re.search(r"%LINK-3-UPDOWN: Interface (\S+), changed state to (\S+)", message)


print("日期 : " + date)
print("设备 : " + hostname)
print("等级 : " + level)
print("接口 : " + result.group(1))
print("状态 : " + result.group(2))
