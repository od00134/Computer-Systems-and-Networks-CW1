import socket
from subprocess import Popen, PIPE
import re


def get_mac_from_ip(address):
    global s, mac
    pid = Popen(["arp", "-n", address], stdout=PIPE)
    s = pid.communicate()[0]
    return re.findall(r"[0-9a-f]{2}(?::[0-9a-f][0-9a-f]){5}", s.decode('utf-8'), re.IGNORECASE)[0]


if __name__ == '__main__':
    s = socket.socket()
    print("Socket successfully created")
    port = 12347
    s.bind(('', port))
    print("socket binded to %s" % (port))
    s.listen(5)
    print("socket is listening")

    # a forever loop until we interrupt it or
    # an error occurs
    while True:
        # Establish connection with client.
        c, addr = s.accept()
        ip_address = addr[0]
        port = addr[1]
        mac = get_mac_from_ip(ip_address)

        c.send(f'IP= {ip_address} and port={port} and mac={mac}'.encode())
        c.close()
        break