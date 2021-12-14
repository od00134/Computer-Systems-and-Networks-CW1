# Import socket module
import socket
if __name__ == '__main__':
    # Create a socket object
    s = socket.socket()

    # Define the port on which you want to connect
    port = 12347

    # connect to the server on local computer
    s.connect(('localhost', port))
    s.sendall(b'HELO server')

    # receive data from the server and decoding to get the string.
    print(s.recv(1024).decode())
    # close the connection
    s.close()
