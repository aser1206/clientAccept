import socket

SERVER_IP="192.168.168.130"
SERVER_PORT = 8080

READ_SIZE = 1024

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    addr = (SERVER_IP,SERVER_PORT)
    
    sock.connect(addr)
    msg_recvd =  sock.recv(READ_SIZE)

    print(msg_recvd.decode())

    sock.close()