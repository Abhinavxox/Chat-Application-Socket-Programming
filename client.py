import socket
import threading

def receive_messages():
    while True:
        message = client_socket.recv(1024).decode()
        print(message)

def send_message():
    while True:
        message = input()
        client_socket.send(message.encode())
        if message == 'exit':
            client_socket.close()
            break

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server's IP address and port number
client_socket.connect(('localhost', 5555))  # Example: using localhost and port 5555

# Start receiving messages from the server
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Start sending messages to the server
send_message()
