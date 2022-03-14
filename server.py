#functionality needed

#receiving jsons
#sending jsons
#connecting to nodes
#disconnecting from nodes

import threading
import socket

#CONSTANTS
SPORT = 25000
DPORT = 25001

IP = socket.gethostbyname( socket.gethostname() )

OTHERIP = input("what is the ip: ")

#create the server for listening
server = socket.socket()
server.bind( ("0.0.0.0", SPORT) )
print( "binded source port...")

#punch hole
server.sendto( b'hole', ( OTHERIP, DPORT) )
print( "sent hole punch" )


# listen for
# equiv: nc -u -l 50001
def listen():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', SPORT))

    while True:
        data = sock.recv(1024)
        print('\rpeer: {}\n> '.format(data.decode()), end='')

listener = threading.Thread(target=listen, daemon=True);
listener.start()

# send messages
# equiv: echo 'xxx' | nc -u -p 50002 x.x.x.x 50001
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', DPORT))

while True:
    msg = input('> ')
    sock.sendto(msg.encode(), (OTHERIP, SPORT))




exit()
#METHODS
#HANDLE CLIENT: handles a certain client
def handle_client(client, ):
    connected = True
    while connected:
        pass

connections = {}

#CONTINOUSLY LISTEN FOR CONNECTIONS
server.listen()
while True:
    connection, address = server.accept()
    print( connection, address )
    
    #thread = threading.Thread(target=handle_client, args=( connection, address) )
    #handle_client(connection, address)

    



