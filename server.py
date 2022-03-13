#functionality needed

#receiving jsons
#sending jsons
#connecting to nodes
#disconnecting from nodes

import threading
import socket

#CONSTANTS
PORT = 7000
IP = socket.gethostbyname( socket.gethostname() )
ADDRESS = (IP, PORT)

#create the server
server = socket.socket()
server.bind( ADDRESS )

#helper methods
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

    



