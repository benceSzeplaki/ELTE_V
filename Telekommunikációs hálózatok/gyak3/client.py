import sys
import struct

i = 1
for i in range(1, len(sys.argv)):
    current_binary_file_name = sys.argv[i]
    with open(current_binary_file_name, "rb") as file:
        if i == 1:
            packer = struct.Struct('?c9s')
            data = file.read(packer.size)
            line = packer.unpack(data)
            first_file = line
        elif i == 2:
            packer = struct.Struct('9sif')
            data = file.read(packer.size)
            line = packer.unpack(data)
            second_file = line
        elif i == 3:
            packer = struct.Struct('fc?')
            data = file.read(packer.size)
            line = packer.unpack(data)
            third_file = line
        else:
            packer = struct.Struct('9s?i')
            data = file.read(packer.size)
            line = packer.unpack(data)
            fourth_factor = line

print(first_file)
print(second_file)
print(third_file)
print(fourth_factor)
packer = struct.Struct('16si?')
print(packer.pack("elso".encode(), 84, True))
packer = struct.Struct('f?c')
print(packer.pack(87.5, False, 'X'.encode()))
packer = struct.Struct('i14sf')
print(packer.pack(75, "masodik".encode(), 94.9))
packer = struct.Struct('ci17s')
print(packer.pack('Z'.encode(), 106, "harmadik".encode()))
