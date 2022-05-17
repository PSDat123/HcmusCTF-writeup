
import pwn
from randcrack import RandCrack

HOST = '103.245.250.31'
PORT = 30620
#####
s = pwn.remote(HOST,PORT)
s.recvuntil('numbers.\n'.encode())
#####
list_num = s.recvline().decode()
list_num = list_num.replace(" ",",").split(",")
list_num = [int(i) for i in list_num]
#####
n = 2**32-2
rc = RandCrack()
random = list_num[41:]

for i in range(len(random)):
    rc.submit(random[i])
ans = rc.predict_randrange(0,n)

s.recvuntil(':\n'.encode())
s.sendline(str(ans).encode())
print(s.recvline())
print(s.recvline())
print(s.recvline())
