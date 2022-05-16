import pwn
from Crypto.Util.number import getPrime,inverse,bytes_to_long,long_to_bytes
from base64 import b64decode, b64encode
from hashlib import sha256
from os import urandom
import random
import numpy as np
import math
HOST = "103.245.250.31"
PORT = 31850

found = False
while not found:
    s = pwn.remote(HOST,PORT)
    s.recvuntil(": ".encode('utf-8'))
    s.sendline('0'.encode('utf-8'))
    g= s.recvline()[4:-1]
    g = int(g.decode())
    p= s.recvline()[4:-1]
    p = int(p.decode())
    ################
    s.recvuntil(": ".encode('utf-8'))
    s.sendline('1'.encode('utf-8'))
    s.recvuntil(": ".encode('utf-8'))
    m1 = b'\01'*32
    m1 = b64encode(m1)
    s.sendline(m1)
    text = s.recvline()[20:-2]
    text = text.decode()
    h1 = bytes_to_long(sha256(m1).digest())
    r1,s1 = text.replace(',','').split(" ")
    r1,s1 = int(r1),int(s1)
    print(r1 , s1)
    print(h1)
    #############
    s.recvuntil(": ".encode('utf-8'))
    s.sendline('1'.encode('utf-8'))
    s.recvuntil(": ".encode('utf-8'))
    m2 = b'\03'*32
    m2 = b64encode(m2)
    s.sendline(m2)
    text1 = s.recvline()[20:-2]
    text1 = text1.decode()
    h2 = bytes_to_long(sha256(m2).digest())
    r2,s2 = text1.replace(',','').split(" ")
    r2,s2 = int(r2),int(s2)
    print(r2 , s2)
    print(h2)
    #######
    Z = Zmod(p-1)
    A = matrix(Z, 2, [[s1, r1],[3*s2,r2]]) 
    y = vector(Z, 2, [h1,h2])
    k,x = A.solve_right(y)
    k = ZZ(k)
    if k % 2 ==0:
        print("fail")
    x = ZZ(x)
    print(pow(g,h1,p)==(pow(pow(g,x,p),r1,p)*pow(r1,s1,p))%p)
    #######
    s.recvuntil(": ".encode('utf-8'))
    s.sendline('3'.encode('utf-8'))
    m3 = s.recvline()[29:-1]
    ######
   
    
    h3 = bytes_to_long(sha256(m3).digest())
    r2 = g
    s3 = (h3 - x*r2) % (p-1)
    print(b64encode(long_to_bytes(r1)))
    print(b64encode(long_to_bytes(s3)))
    
    s.recvuntil(": ".encode('utf-8'))
    s.sendline(b64encode(long_to_bytes(r2)))
    s.recvuntil(": ".encode('utf-8'))
    s.sendline(b64encode(long_to_bytes(s3)))   
    ans = s.recvline()
    print(ans)
    if "Congratulation" in ans.decode():
        print(ans)
        break
        s.close()
    else:
        s.close()
