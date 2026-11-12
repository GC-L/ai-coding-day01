import time
from getpass import getpass

import paramiko


def read_until_prompt(chan, timeout=10):
    """一直读，直到结尾出现提示符 # 或 >；超过 timeout 秒就报错。"""
    result = ""
    start = time.time()
    while True:
        if chan.recv_ready():
            result += chan.recv(65535).decode()

        if result.rstrip().endswith(("#", ">")):
            return result                          # 看到提示符：读完了

        if time.time() - start > timeout:
            raise TimeoutError("超时了，没等到提示符")

        time.sleep(0.1)                            # 稍等一下再看


def qytang_multicmd(ip, username, password, cmd_list, wait_time=2, verbose=True):
    """在同一个SSH交互终端依次执行cmd_list，返回全部回显文本。"""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=username, password=password,
                look_for_keys=False, allow_agent=False)

    try:
        chan = ssh.invoke_shell()
        read_until_prompt(chan)                    # 读掉欢迎信息

        output = ""
        for cmd in cmd_list:
            chan.sendall((cmd + "\n").encode())
            result = read_until_prompt(chan)
            output += result
            if verbose:
                print(result, end="")
        if verbose:
            print()
        return output
    finally:
        ssh.close()


if __name__ == "__main__":
    cmd_list = [
        'terminal length 0',
        'show version | include Software,',
        'show running-config | include hostname',
    ]
    qytang_multicmd('10.1.1.1', 'admin', getpass('SSH密码：'), cmd_list)