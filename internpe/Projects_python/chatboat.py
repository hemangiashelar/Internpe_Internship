import tkinter as tk
from tkinter import Scrollbar, Text

class Chatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")
        
        self.create_ui()

    def create_ui(self):
        self.chat_history = Text(self.root, font=('Helvetica', 12), wrap='word', state='disabled', height=20, width=50)
        self.chat_history.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        self.scrollbar = Scrollbar(self.root, command=self.chat_history.yview)
        self.scrollbar.grid(row=0, column=2, sticky='nsew')
        
        self.chat_history['yscrollcommand'] = self.scrollbar.set
        
        self.input_text = tk.Entry(self.root, font=('Helvetica', 12), width=40)
        self.input_text.grid(row=1, column=0, padx=10, pady=10)
        
        self.send_button = tk.Button(self.root, text='Send', font=('Helvetica', 12), command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)

        self.greeting_message()

    def greeting_message(self):
        message = "Chatbot: Hello! I am your friendly chatbot. How can I assist you today?"
        self.display_message(message)

    def send_message(self):
        user_message = self.input_text.get()
        self.display_message(f"You: {user_message}")

        response = self.get_bot_response(user_message)
        
        self.display_message(response)
        self.input_text.delete(0, 'end')

    def get_bot_response(self, user_message):
        if "hello" in user_message.lower() or "hi" in user_message.lower():
            return "Chatbot: Hi there! I'm doing well. How can I help you?"
        else:
            return "Chatbot: I'm just a basic chatbot. Sorry, I don't have a specific answer for that."

    def display_message(self, message):
        self.chat_history.config(state='normal')
        self.chat_history.insert('end', message + '\n')
        self.chat_history.config(state='disabled')
        self.chat_history.see('end')

def main():
    root = tk.Tk()
    app = Chatbot(root)
    root.mainloop()

if __name__ == "__main__":
    main()
