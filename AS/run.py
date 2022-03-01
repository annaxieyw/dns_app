import socket

store = {}
sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
sock.bind(('', 53533))
while True:
    mes, ad = sock.recvfrom(2048)
    dc = mes.decode()
    sdc = dc.split('\n')
    name = sdc[1].split('=')[1]
    if 'VALUE' in dc: 
        value = sdc[2].split('=')[1]
        store[name] = value
        sock.sendto("Success".encode(), ad)
    else: 
        if name in store:
            response = "TYPE=A\nNAME={}\nVALUE={}\nTTL=10".format(name,store[name])
            sock.sendto(response.encode(), ad)
