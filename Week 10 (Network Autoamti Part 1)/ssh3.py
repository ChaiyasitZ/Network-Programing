from netmiko import ConnectHandler

SW4 = {
    'device_type': 'cisco_ios',
    'ip': '10.4.15.60',
    'username': 'cisco',
    'password': 'cisco'
}

SW5 = {
    'device_type': 'cisco_ios',
    'ip': '10.4.15.60',
    'username': 'cisco',
    'password': 'cisco'
}

f = open("myswitches")
lines = f.read().splitlines()

all_devices = [SW4, SW5]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print(output)