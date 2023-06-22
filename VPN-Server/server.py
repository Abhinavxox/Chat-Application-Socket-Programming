import socket
import ssl

# Define the server address and port
server_address = ('127.0.0.1', 6969)

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server address and port
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print('Server is listening for connections...')

while True:
    # Accept incoming connections
    client_socket, client_address = server_socket.accept()
    print(f'Client connected from {client_address}')

    # Wrap the socket with SSL/TLS
    ssl_socket = ssl.wrap_socket(client_socket, server_side=True, certfile='server.crt', keyfile='server.key', ssl_version=ssl.PROTOCOL_TLS)

    # Handle client communication here...
    while True:
        try:
            # Receive data from the client
            data = ssl_socket.recv(1024)
            if not data:
                break

            # Process the received data
            # Example: Echo the data back to the client
            ssl_socket.sendall(data)
        except ssl.SSLError:
            break

    # Close the SSL/TLS socket
    ssl_socket.close()
