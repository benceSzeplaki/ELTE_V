import sys
import struct
import socket

packer = struct.Struct('20si')

if len(sys.argv) == 3:
    if str(sys.argv[1]) == 'port':
        with open("domainPort.bin", "rb") as f:
            f.seek(packer.size * int(sys.argv[2]))
            data = f.read(packer.size)
            line = packer.unpack(data)
            print(line[1])
            print(socket.getservbyport(int(line[1])))
    elif str(sys.argv[1]) == 'domain':
        with open("domainPort.bin", "rb") as f:
            f.seek(packer.size * int(sys.argv[2]))
            data = f.read(packer.size)
            line = packer.unpack(data)
            print(line[0].decode().strip('\x00'))
            print(socket.gethostbyname(str(line[0].decode().strip('\x00'))))
    else:
        print(socket.gethostname())
else:
    print(socket.gethostname())
