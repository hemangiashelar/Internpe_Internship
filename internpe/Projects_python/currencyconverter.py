import tkinter as tk
from tkinter import messagebox

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        self.create_ui()

    def create_ui(self):
        amount_label = tk.Label(self.root, text="Amount:", font=("Helvetica", 26))
        amount_label.pack()

        self.amount_entry = tk.Entry(self.root, font=("Helvetica", 26))
        self.amount_entry.pack()

        convert_button = tk.Button(self.root, text="Convert", command=self.convert, bg="green", fg="white", font=("Helvetica", 14), width=15)
        convert_button.pack(pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 20))
        self.result_label.pack()

    def convert(self):
        amount = self.amount_entry.get()
        
        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")
            return

        converted_amount = amount * 0.85  # Simple conversion rate for demonstration purposes
        self.result_label.config(text=f"Converted Amount: {converted_amount:.2f} USD")

def main():
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
