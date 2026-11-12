import time
from getpass import getpass

import paramiko


def qytang_multicmd(ip, username, password, cmd_list, wait_time=2, verbose=True):
    """在同一个SSH交互终端依次执行cmd_list，返回全部回显文本。"""
    # 1. 登录设备
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=username, password=password,
                look_for_keys=False, allow_agent=False)

    try:
        # 2. 打开交互终端，读掉欢迎信息
        chan = ssh.invoke_shell()
        chan.settimeout(10)          # recv 最多等 10 秒，防止死等
        time.sleep(1)
        chan.recv(65535)

        # 3. 逐条执行：发命令 → 等待 → 把能读的都读完
        output = ""
        for cmd in cmd_list:
            chan.sendall((cmd + "\n").encode())
            time.sleep(wait_time)
            result = ""
            while chan.recv_ready():     # 快递柜里还有东西，就继续取
                result += chan.recv(65535).decode()
            output += result
            if verbose:
                print(result, end="")
        if verbose:
            print()
        return output
    finally:
        # 4. 不管中间有没有出错，最后都断开连接
        ssh.close()


if __name__ == "__main__":
    cmd_list = [
        'terminal length 0',
        'show version | include Software,',
        'show running-config | include hostname',
    ]
    qytang_multicmd('10.1.1.1', 'admin', getpass('SSH密码：'), cmd_list)