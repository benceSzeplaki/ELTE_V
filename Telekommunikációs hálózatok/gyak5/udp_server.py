import struct
from socket import socket, AF_INET, SOCK_DGRAM

server_addr = ('', 10000)

def validate_data(data):
    error = ""
    packer = struct.Struct('iic')
    real_data = packer.unpack(data)
    if real_data[0] != type(int):
        error = "TypeError on first int"
    elif real_data[1] != type(int):
        error = "TypeError on second int"
    elif real_data[2] != type(str):
        error = "TypeError on operator"
    else:
        if real_data[2] is not '-' or '+' or '/' or '*':
            error = "Invalid operator"
    return error


def doMathBitch(param, param1, param2):
    if param2 is '-':
        return param - param1
    elif param2 is '+':
        return param + param2
    elif param2 is '/':
        return param / param2
    elif param2 is '*':
        return param * param2

with socket(AF_INET, SOCK_DGRAM) as server:
    server.bind(server_addr)

    data, client_address = server.recvfrom(200)
    print("Kaptam: ", data, "Tole: ", client_address)
    error = validate_data(data)
    if error is not "":
        server.sendto(error, client_address)
    else:
        packer = struct.Struct('iic')
        real_data = packer.unpack(data)
        server.sendto(doMathBitch(real_data[0], real_data[1], real_data[2].encode(), client_address))

    server.sendto("Hello kliens".encode(), client_address)
