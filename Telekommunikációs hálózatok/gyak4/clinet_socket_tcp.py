from socket import socket, AF_INET, SOCK_STREAM
from time import sleep

server_address = ('localhost', 10000)

with socket(AF_INET, SOCK_STREAM) as client:
    # AF_NET = ipv4, SOCK_STREAM = TCP kapcsolat
    client.connect(server_address)

    client.sendall("Hello szejvej!".encode())
    data = client.recv(200)
    print("Kapta: ", data.decode())
    sleep(1)
