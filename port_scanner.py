import socket
import time


def check_port(ip, port):
    try:
        sock = socket.socket()
        sock.connect((ip, port))
    except:
        return False
    else:
        return True
    finally:
        sock.close()


if __name__ == '__main__':
    ip = 'hackthissite.org'
    tic = time.time()
    print('#' * 50)
    for port in range(1, 1025):
        if check_port(ip, port):
            print('Port', port, 'is open')
        else:
            print('Port', port, 'is closed')
    print('#' * 50)
    toc = time.time()
    print('Total time: {:.2f} seconds'.format(toc - tic))
    # Total time: ~21,504 seconds (around 6 hours)
