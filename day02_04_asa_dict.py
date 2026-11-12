import re

asa_conn = """TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO
TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"""

# 第 1 步：准备一个空字典，用来存解析结果
conn_dict = {}

# 第 2 步：按换行符拆成多行，逐行解析
for line in asa_conn.split("\n"):
    result = re.match(
        r"\S+\s+Student\s+([\d.]+):(\d+)\s+Teacher\s+([\d.]+):(\d+),.*bytes\s+(\d+),\s+flags\s+(\S+)",
        line,
    )
    # 键：(源IP, 源端口, 目的IP, 目的端口)；值：(bytes, flags)
    key = (result.group(1), result.group(2), result.group(3), result.group(4))
    value = (result.group(5), result.group(6))
    conn_dict[key] = value

# 第 3 步：直接打印整个字典
print("打印分析后的字典!\n")
print(conn_dict)

# 第 4 步：遍历字典，格式化打印报告
print("\n格式化打印输出\n")
for key, value in conn_dict.items():
    print("{:<10}: {:<17}| {:<10}: {:<7}| {:<10}: {:<17}| {:<10}: {}".format(
        "src", key[0], "src_port", key[1], "dst", key[2], "dst_port", key[3]))
    print("{:<10}: {:<17}| {:<10}: {}".format("bytes", value[0], "flags", value[1]))
    print("=" * 84)