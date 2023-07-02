import socket
import tkinter as tk
import threading

# Server configuration
HOST = '127.0.0.1'  # Server IP address
PORT = 5000  # Server port number

class Client:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.gui_thread = None

    def start(self):
        self.client_socket.connect((HOST, PORT))
        print('Connected to the server.')

        self.gui_thread = threading.Thread(target=self.create_gui)
        self.gui_thread.start()

        self.gui_thread.join()

    def create_gui(self):
        root = tk.Tk()
        root.title('Client')

        message_label = tk.Label(root, text='Message:')
        message_label.pack()

        message_entry = tk.Entry(root)
        message_entry.pack()

        send_button = tk.Button(root, text='Send', command=lambda: self.send_message(message_entry.get()))
        send_button.pack()

        root.mainloop()

    def send_message(self, message):
        self.client_socket.send(message.encode('utf-8'))
        print(f'Message sent: {message}')


if __name__ == '__main__':
    client = Client()
    client.start()
