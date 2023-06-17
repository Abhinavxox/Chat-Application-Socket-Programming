# client.py

import socket
import threading
import tkinter as tk

def receive_messages():
    while True:
        message = client_socket.recv(1024).decode()
        chat_box.insert(tk.END, message + '\n')

def send_message(event=None):
    message = input_box.get()
    input_box.delete(0, tk.END)
    client_socket.send(message.encode())
    if message == 'exit':
        client_socket.close()

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server's IP address and port number
client_socket.connect(('localhost', 5555))  # Example: using localhost and port 5555

# Create the GUI
window = tk.Tk()
window.title("Group Chat")

# Create the chat box
chat_box = tk.Text(window)
chat_box.pack()

# Create the input box
input_box = tk.Entry(window)
input_box.pack()

# Set focus on the input box
input_box.focus()

# Bind the Enter key to send messages
window.bind('<Return>', send_message)

# Start receiving messages from the server
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Start the GUI main loop
window.mainloop()
