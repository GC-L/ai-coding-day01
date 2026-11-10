version_raw = "  Cisco IOS XE Software, Version 17.03.04  "
s=version_raw.strip()
print("去掉空格: " + s)
print("转大写:   " + s.upper())
print("替换版本: " + s.replace("17.03.04", "17.06.01"))