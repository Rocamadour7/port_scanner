import socket
import time
import threading
from queue import Queue

print_lock = threading.Lock()
queue = Queue()


def check_port(port):
    sock = socket.socket()
    try:
        sock.connect((ip, port))
        with print_lock:
            print('Port', port, 'is open')
    except:
        with print_lock:
            print('Port', port, 'is closed')
    finally:
        sock.close()


def threader():

    while True:
        worker = queue.get()
        check_port(worker)
        queue.task_done()


if __name__ == '__main__':
    for _ in range(30):
        thread = threading.Thread(target=threader)
        thread.daemon = True
        thread.start()

    ip = 'hackthissite.org'

    print('#' * 50)
    print('Scanning {}'.format(ip))
    tic = time.time()
    print('#' * 50)
    for worker in range(1, 1025):
        queue.put(worker)
    queue.join()
    print('#' * 50)
    toc = time.time()
    print('Total time: {:.2f} seconds'.format(toc - tic))
    # Total time: 735.11 seconds local ip
    # Total time: 735.11 seconds hackthissite.org
