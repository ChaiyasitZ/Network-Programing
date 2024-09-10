import paramiko
import threading
import os.path
import subprocess
import time
import sys
import re

def ip_is_valid():
    check = False
    global ip_list
    
    while True:
        
        print("####################\n")
        ip_file = input("# Enter IP file path and name (e.g. D:\MyApps\myfile.txt): ")
        print("####################\n")
        
        try:
            selected_ip_file = open(ip_file, 'r')
            selected_ip_file.seek(0)
            ip_list = selected_ip_file.readlines()
            selected_ip_file.close()
            
        except FileNotFoundError as e:
            print('*** Found Python Traceback Error', e)
            print('*** Please check the file path and try again\n'% ip_file)
        
        try:
            for ip in ip_list:
                a = ip.split('.')
                if (len(a) == 4) and (1 <= int(a[0]) <= 223) and (int(a[0]) != 127) and (int(a[0]) != 169 or int(a[1]) != 254) and (0 <= int(a[1]) <= 255 
                and 0 <= int(a[2]) <= 255 and 0 <= int(a[3]) <= 255):
                    print('The current IP address is valid: %s\n', a)
                    check = True
                    continue
                    
                else:
                    print('The current IP address is valid: %s\n', a)
                    print('*** Please check the file again\n')
                    check = False
                    break
        
        except NameError:
            continue
        
        if check == False:
            print('Go to While loop\n')
            continue
        
        elif check == True:
            print("All IP addresses in 'ssh-ip.txt' file are valid")
            break   

        print("Please wait...\n")
        
        check2 = False
        
        while True:
            for ip in ip_list:           
                ping_reply = subprocess.call(['ping', '-n', '-c', '2', '-w', '1', ip])
                
                if ping_reply == 0:
                    check2 = True
                    continue
                
                elif ping_reply == 2:
                    print('*** No response from IP address %s' % ip)
                    check2 = False
                    break
                
                else:
                    print('*** {} not reachable. Check connectivity and try again.'.format(ip))
                    check2 = True
                    break
                
            if check2 == False:
                print('re-check IP address\n')
                ip_is_valid()
            
            elif check2 == True:
                print('All IP addresses are reachable\n')
                break

def user_is_valid():
    global user_file
    
    while True:
        print("####################\n")
        user_file = input("# Enter username file path and name (e.g. D:\MyApps\myfile.txt): ")
        print("####################\n")
        
        if os.path.isfile(user_file) == True:
            print("Username file is valid\n")
            break
        
        else:
            print("Username file is invalid. Please check the file and try again\n")
            continue

def cmd_is_valid():
    global cmd_file
    
    while True:
        print("####################\n")
        cmd_file = input("# Enter command file path and name (e.g. D:\MyApps\myfile.txt): ")
        print("####################\n")
        
        if os.path.isfile(cmd_file) == True:
            print("Command file is valid\n")
            break
        
        else:
            print("Command file is invalid. Please check the file and try again\n")
            continue

try:
    ip_is_valid()

except KeyboardInterrupt:
    print("\nProgram aborted by user. Exiting...\n")
    sys.exit()
    
try:
    cmd_is_valid()

except KeyboardInterrupt:
    print("\nProgram aborted by user. Exiting...\n")
    sys.exit()

def open_ssh_conn(ip):
    try:
        selected_user_file = open(user_file, 'r')
        selected_user_file.seek(0)
        username = selected_user_file.readlines()[0].split(',')[0]
        selected_user_file.seek(0)
        password = selected_user_file.readlines()[0].split(',')[1].rstrip("\n")
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip, username = username, password = password, allow_agent=False, look_for_keys=False)
        connection = session.invoke_shell()
        selected_cmd_file = open(cmd_file, 'r')
        selected_user_file.seek(0)
        
        for each_line in selected_cmd_file.readlines():
            connection.send(each_line + '\n')
            time.sleep(2)
            
        selected_user_file.close()
        selected_cmd_file.close()
        router_output = connection.recv(65535)
        
        if re.search(r"% Invalid input" , str(router_output, 'utf-8')):
            print('*** Invalid input detected. Closing connection...%s\n' % ip)
        
        else:
            print('*** Success. Closing connection...%s\n' % ip)
        
        print(str(router_output, 'utf-8') + '\n')
        
        session.close()
    
    except paramiko.AuthenticationException:
        print('*** Invalid username or password. Please check the username/password file or the device configuration.')
        print('*** Closing connection...\n')

def create_threads():
    threads = []
    
    for ip in ip_list:
        ip = ip.rstrip()
        th = threading.Thread(target = open_ssh_conn, args = (ip,))
        th.start()
        threads.append(th)
        
    for th in threads:
        th.join()

create_threads()
        
        
        
