import socket
import threading

def handle_client(client_socket, client_address):
    while True:
        message = client_socket.recv(1024).decode()
        if message == 'exit':
            clients.remove(client_socket)
            client_socket.close()
            break
        else:
            broadcast(message, client_socket)

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            client.send(message.encode())

def accept_connections():
    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific IP address and port number
server_socket.bind(('localhost', 5555))  # Example: using localhost and port 5555

# Listen for incoming connections
server_socket.listen(5)  # Maximum number of queued connections

# Create a list to store connected clients
clients = []

# Start accepting client connections
accept_connections()
