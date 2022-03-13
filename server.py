import socket

server = socket.socket()

server.bind( ( socket.gethostname() , 7000) )
server.listen()

input("PRESS ENTER")

while True:
    clientsocket, address = server.accept()
    print( f"connection from {address} has been made" )
    
    clientsocket.send(bytes("hello!", "utf-8") )


def send_data( address ):
    clientsocket.send

