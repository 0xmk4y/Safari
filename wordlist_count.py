
import threading
import time
import sys

#Wordlist length
def passwd_list_len():
    with open('/usr/share/wordlists/rockyou.txt', errors="replace" ) as f:
        return len(f.readlines())


start = time.perf_counter()
    

print(passwd_list_len())
    
    
finish = time.perf_counter()
print(round(finish - start,2))