import logging
import socket
import select

logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)

def create_nonblocking(host, port):
    logging.info('Non Blocking - Creating socket')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    logging.info('Non Blocking - connecting')
    ret = s.connect_ex((host, port))
    
    print('ret:', ret)
    if ret != 0:
        logging.info('Non Blocking - Failed to connect!')
        return
    
    logging.info('Non Blocking - connected')
    s.setblocking(False)
    
    inputs = [s]
    print('inputs:', inputs)
    outputs = [s]
    print('outputs:', outputs)
    
    while inputs:
        logging.info('Non Blocking - Waiting...')
        readable, writable, exceptional = select.select(
            inputs, outputs, inputs, 0.5
        )
        
        print('readable:', readable)
        print('writable:', writable)
        print('exceptional:', exceptional)
        
        for s in readable:
            logging.info('Non Blocking - Reading...')
            data = s.recv(1024)
            logging.info(f'Non Blocking - data= {len(data)}')
            logging.info('Non Blocking - Closing')
            s.close()
            inputs.remove(s)
            break
        for s in writable:
            logging.info('Non Blocking - Sending...')
            s.sendall(b'Hello, world')
            logging.info('Non Blocking - Closing')
            s.close()
            outputs.remove(s)
            break
        for s in exceptional:
            logging.info('Non Blocking - Error!')
            s.close()
            inputs.remove(s)
            outputs.remove(s)
            break

def main():
    create_nonblocking('github.com', 80)

if __name__ == '__main__':
    main()