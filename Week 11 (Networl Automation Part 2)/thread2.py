import threading
from queue import Queue
from getpass import getpass
from netmiko import ConnectHandler

USER = 'cisco'
PASSWORD = 'cisco'

routers = ['']

def ssh_session(router, output_q):
    output_dict = {}
    hostname = router
    router = {
        'device_type': 'cisco_ios',
        'ip': router,
        'username': USER,
        'password': PASSWORD,
        'verbose': False,
    }
    ssh_session = ConnectHandler(**router)
    output = ssh_session.send_command('show version')
    output_dict[hostname] = output
    output_q.put(output_dict)