from tkinter import Tk, Text, Entry, Button, Scrollbar

class ChatApplication:
    def __init__(self):
        self.window = Tk()
        self.window.title("Chat Window")

        self.chat_textbox = Text(self.window, height=20, width=50)
        self.scrollbar = Scrollbar(self.window, command=self.chat_textbox.yview)
        self.chat_textbox.configure(yscrollcommand=self.scrollbar.set)
        self.input_entry = Entry(self.window)
        self.send_button = Button(self.window, text="Send", command=self.send_message)

        self.chat_textbox.pack(side='top', padx=10, pady=10)
        self.scrollbar.pack(side='right', fill='y')
        self.input_entry.pack(side='left', padx=10)
        self.send_button.pack(side='left')

    def send_message(self):
        message = self.input_entry.get()
        if message:
            self.chat_textbox.insert('end', f"You: {message}\n")
            self.input_entry.delete(0, 'end')

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = ChatApplication()
    app.run()
