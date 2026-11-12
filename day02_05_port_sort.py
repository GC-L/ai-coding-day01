import re

port_list = [
    'eth 1/101/1/42',
    'eth 1/101/1/26',
    'eth 1/101/1/23',
    'eth 1/101/1/7',
    'eth 1/101/2/46',
    'eth 1/101/1/34',
    'eth 1/101/1/18',
    'eth 1/101/1/13',
    'eth 1/101/1/32',
    'eth 1/101/1/25',
    'eth 1/101/1/45',
    'eth 1/101/2/8',
]

# 用正则取出第 3、4 段编号，转成整数组成元组，作为排序依据
port_list.sort(key=lambda port: tuple(map(int, re.match(r"eth\s+\d+/\d+/(\d+)/(\d+)", port).groups())))

print(port_list)