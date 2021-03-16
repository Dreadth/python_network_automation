import pexpect

device_list = [
    {
        'ip': '10.13.37.1',
        'vendor': 'cisco',
        'tags': 'router'
    },
    {
        'ip': '10.13.37.2',
        'vendor': 'cisco',
        'tags': 'router'
    },
    {
        'ip': '10.13.37.11',
        'vendor': 'cisco',
        'tags': 'switch'
    },
    {
        'ip': '10.13.37.12',
        'vendor': 'cisco',
        'tags': 'switch'
    },
    {
        'ip': '10.13.37.13',
        'vendor': 'cisco',
        'tags': 'switch'
    }
]

username = 'dreadth'
password = 'helloworld'
enable_password = 'helloworld'


def cisco_login(pexpect_spawn):
    pexpect_spawn.expect('Username')
    pexpect_spawn.sendline(username)
    pexpect_spawn.expect('Password')
    pexpect_spawn.sendline(password)
    pexpect_spawn.expect('>')
    name = pexpect_spawn.before.decode().replace(':', "").strip()
    pexpect_spawn.sendline('enable')
    pexpect_spawn.expect('Password')
    pexpect_spawn.sendline(enable_password)
    pexpect_spawn.expect('#')
    pexpect_spawn.sendline('terminal length 0')
    pexpect_spawn.expect('#')
    return name


def cisco_exit(pexpect_spawn):
    pexpect_spawn.sendline('exit')


def cisco_send_cli_return_output(pexpect_spawn, cmd):
    pexpect_spawn.sendline(cmd)
    pexpect_spawn.expect('#')
    value = pexpect_spawn.before
    return value.decode().strip(cmd).replace('\r', '').split('\n')[1]


for device in device_list:
    spawn = pexpect.spawn(f'telnet {device["ip"]}')
    device_name = cisco_login(spawn)
    print(cisco_send_cli_return_output(spawn, 'show clock'), f'[{device_name}]')
    cisco_exit(spawn)
