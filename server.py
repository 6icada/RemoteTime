# Code by 6icada
# Please do not copy code

# tring to import libraries
try:
    import socket
    from datetime import datetime
    import time
except:
    # ERROR MSG
    print('[ERROR]: Can\'t import libraries')

# MakeSocket function
def MakeSocket():
    # Adding vars
    HOST = '127.0.0.1'
    PORT = 4444
    clients = []
    clientsHistory = []

    # Binding Server_Socket
    Server_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Server_Socket.bind((HOST, PORT))
    Server_Socket.listen()
    
    # MSG when server starts
    print(f'[START]: Time server is running on {HOST}:{PORT}')

    # Handle function (To Handle clients and send date to them)
    def Handle():
        while True:
            # Adding vars
            now = datetime.now()
            timeToSend = now.strftime("%d/%m/%Y %H:%M:%S")
            client, address = Server_Socket.accept()

            # Adding client's address and port to clients list and clientsHistory list
            clients.append(address)
            clientsHistory.append(address)

            # MSG when client connects
            print(f'[INFO]: Connection from {address}')
            
            # Sendig date to client
            client.send(f'Date: {timeToSend}'.encode('utf-8'))
            
            try:
                # Removing clien from clients list
                clients.remove(client)
            except:
                pass

    # Calling functions
    Handle()

# Calling functions
MakeSocket()
