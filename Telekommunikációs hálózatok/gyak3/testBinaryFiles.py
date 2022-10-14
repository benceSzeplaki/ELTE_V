import struct

var = struct.pack('?c9s', True, 'a'.encode(), "abcdefghi".encode())
print(var)
print(struct.unpack('?c9s', var))
with open('db1.bin', 'wb') as file:
    file.write(var)

var = struct.pack('9sif', "abcdefghi".encode(), 1, 1.1)
print(var)
print(struct.unpack('9sif', var))
with open('db2.bin', 'wb') as file:
    file.write(var)

var = struct.pack('fc?', 1.123456, 'a'.encode(), True)
print(var)
print(struct.unpack('fc?', var))
with open('db3.bin', 'wb') as file:
    file.write(var)

var = struct.pack('9s?i', "abcdefghi".encode(), False, 2)
print(var)
print(struct.unpack('9s?i', var))
with open('db4.bin', 'wb') as file:
    file.write(var)
