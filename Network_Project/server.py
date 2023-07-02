import socket
import threading
import tkinter as tk

# Server configuration
HOST = '127.0.0.1'  # Server IP address
PORT = 5000 # Server port number

class Server:
    def __init__(self):
        self.clients = []  # Store connected clients
        self.server_socket = None
        self.gui_thread = None

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((HOST, PORT))
        self.server_socket.listen(5)
        print('Server started.')

        self.gui_thread = threading.Thread(target=self.create_gui)
        self.gui_thread.start()

        while True:
            client_socket, addr = self.server_socket.accept()
            self.clients.append((client_socket, addr))
            print(f'New client connected: {addr}')
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        while True:
            try:
                data = client_socket.recv(1024).decode('utf-8')
                if data:
                    print(f'Message received: {data}')
                    self.broadcast_message(data, client_socket.getpeername())

            except ConnectionResetError:
                self.clients = [client for client in self.clients if client[0] != client_socket]
                print(f'Client disconnected: {client_socket.getpeername()}')
                client_socket.close()
                break

    def broadcast_message(self, message, source_addr):
        for client in self.clients:
            client_socket, addr = client
            if client_socket.getpeername() != source_addr:
                client_socket.send(f'{source_addr}: {message}'.encode('utf-8'))

        # Update GUI chat window
        self.gui_chat_text.configure(state='normal')
        self.gui_chat_text.insert(tk.END, f'{source_addr}: {message}\n')
        self.gui_chat_text.configure(state='disabled')

    def create_gui(self):
        root = tk.Tk()
        root.title('Server')

        frame = tk.Frame(root)
        frame.pack(fill='both', expand=True)

        chat_frame = tk.Frame(frame, bg='white')
        chat_frame.pack(side='left', fill='both', expand=True)

        chat_label = tk.Label(chat_frame, text='Group Chat')
        chat_label.pack()

        self.gui_chat_text = tk.Text(chat_frame, state='disabled')
        self.gui_chat_text.pack(fill='both', expand=True)

        attendance_frame = tk.Frame(frame, bg='white')
        attendance_frame.pack(side='right', fill='y')

        attendance_label = tk.Label(attendance_frame, text='Attendance')
        attendance_label.pack()

        attendance_listbox = tk.Listbox(attendance_frame)
        attendance_listbox.pack(fill='y')

        def update_attendance_list():
            attendance_listbox.delete(0, tk.END)
            for client in self.clients:
                client_socket, addr = client
                attendance_listbox.insert(tk.END, addr)
            root.after(1000, update_attendance_list)

        root.after(1000, update_attendance_list)
        root.mainloop()


if __name__ == '__main__':
    server = Server()
    server.start()
