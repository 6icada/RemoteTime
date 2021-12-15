# Code by 6icada
# Please do not copy code

# Tring to import libraries
try:
    import socket
except:
    # ERROR MSG
    print('[ERROR]: Can\'t import libraries')

# Adding vars
HOST = '127.0.0.1'
PORT = 4444

# Making Client_Socket
Client_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting to the server
Client_Socket.connect((HOST, PORT))

encodedData = Client_Socket.recv(1024)

# Printing time
print(encodedData.decode('utf-8'))

# Closing connection
Client_Socket.close()
exit()
