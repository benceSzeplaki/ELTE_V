import struct
from socket import socket, AF_INET, SOCK_DGRAM
from struct import Struct

server_addr = ('localhost', 10000)

with socket(AF_INET, SOCK_DGRAM) as client:
    packer = struct.Struct('iic')
    p = packer.pack(1, 1, '+'.encode())

    client.sendto(p, server_addr)

    data, _ = client.recvfrom(200)

    print("Kaptam: ", data.decode())
