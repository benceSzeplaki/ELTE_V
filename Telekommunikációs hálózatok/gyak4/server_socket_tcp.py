from socket import socket, AF_INET, SOCK_STREAM
from select import select

# Szerver letrehozas
server_address = ('localhost', 10000)

# Socket szerver letrehozas
with socket(AF_INET, SOCK_STREAM) as server:
    # A letrehozott socket tomb
    inputs = [server]
    server.bind(server_address)
    server.listen(1)

    while True:
        # azt nezi meg h kik azok akik varakoznak, kuldenek, vagy errort dobnak
        timeout = 1
        r, w, e = select(inputs, inputs, inputs, timeout)

        if not (r or w or e):
            continue

        for s in r:
            if s is server:
                client, client_address = s.accept()
                inputs.append(client)
                print("Kapcsolodott: ", client_address)
            else:
                data = s.recv(200)
                if not data:
                    print("Kilepett", s)
                    inputs.remove(s)
                    s.close()
                else:
                    print("Kapta, halt", data.decode())
                    s.sendall("OK".encode())
