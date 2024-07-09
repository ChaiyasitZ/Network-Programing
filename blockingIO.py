import logging
import socket

logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)

# Blocking
def create_blocking(host, ip):
    logging.info('Blocking - Creating socket')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    logging.info('Blocking - Connecting to server')
    s.connect((host, ip))  
    logging.info('Blocking - conected')
    logging.info('Blocking - Sending...')
    s.sendall(b'Hello, world')
    logging.info('Blocking - waiting...')
    data = s.recv(1024)
    logging.info(f'Blocking - data= {len(data)}')
    logging.info('Blocking - closing')
    s.close()
    
def main():
    create_blocking('github.com', 80)

if __name__ == '__main__':
    main()