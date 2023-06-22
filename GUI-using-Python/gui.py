# gui.py

import subprocess
import tkinter as tk

def run_server():
    subprocess.Popen(['python3', 'server.py'])

def run_client():
    subprocess.Popen(['python3', 'client.py'])

# Create the GUI
window = tk.Tk()
window.title("Chat Application")

# Create the server button
server_button = tk.Button(window, text="Start Server", command=run_server)
server_button.pack()

# Create the client buttons
client1_button = tk.Button(window, text="Start Client 1", command=run_client)
client1_button.pack()

client2_button = tk.Button(window, text="Start Client 2", command=run_client)
client2_button.pack()

# Start the GUI main loop
window.mainloop()
