from getpass import getpass

from day04_01_multicmd import qytang_multicmd
from day04_02_ping_check import ping_check

hosts = ['10.1.1.1', '10.1.1.2', '10.1.1.3']
RIP_COMMANDS = [
    'configure terminal',
    'router rip',
    'version 2',
    'network 172.16.0.0',
    'end',
]

if __name__ == "__main__":
    username = 'admin'
    password = getpass('SSH密码：')

    for host in hosts:
        ok, _ = ping_check(host)
        if ok:
            print(f"[{host}] ping通，开始配置RIP")
            qytang_multicmd(host, username, password, RIP_COMMANDS)
            print(f"[{host}] RIP命令执行完成\n")
        else:
            print(f"[{host}] ping不通，跳过SSH")