byte = b'Hello World \x32 \x9e'

for b in byte:
    print(chr(b), b, hex(b))