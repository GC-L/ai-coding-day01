import time, paramiko
from getpass import getpass


def qytang_multicmd(ip, username, password, cmd_list, wait_time=2, verbose=True):
    """在同一个SSH交互终端依次执行cmd_list，返回全部回显文本。"""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)
    chan = ssh.invoke_shell()
    time.sleep(1)
    chan.recv(65535)   # 读掉登录欢迎信息
    for cmd in cmd_list:
        chan.sendall((cmd + "\n").encode())      # \n 相当于回车
        time.sleep(wait_time)
        print(chan.recv(65535).decode(), end="")
    ssh.close()
    print()

if __name__ == "__main__":
    cmd_list = [
        'terminal length 0',
        'show version | include Software,',
        'show running-config | include hostname',
    ]
    qytang_multicmd('10.1.1.1', 'admin', getpass('SSH密码：'), cmd_list)