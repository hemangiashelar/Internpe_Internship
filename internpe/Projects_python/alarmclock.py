import tkinter as tk
import time
from tkinter import messagebox

class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")
        
        self.alarm_time = tk.StringVar()
        self.create_ui()

    def create_ui(self):
        self.label = tk.Label(self.root, text="Set Alarm Time (HH:MM:SS):", font=("Helvetica", 14))
        self.label.pack()

        self.entry = tk.Entry(self.root, textvariable=self.alarm_time, font=("Helvetica", 12))
        self.entry.pack()

        self.set_button = tk.Button(self.root, text="Set Alarm", command=self.set_alarm, font=("Helvetica", 12), width=15)
        self.set_button.pack(pady=10)

        self.stop_button = tk.Button(self.root, text="Stop Alarm", command=self.stop_alarm, font=("Helvetica", 12), width=15)
        self.stop_button.pack(pady=5)

    def set_alarm(self):
        alarm_time = self.alarm_time.get()
        self.alarm_seconds = self.convert_to_seconds(alarm_time)

        if self.alarm_seconds < 0:
            messagebox.showerror("Error", "Invalid time format")
            return

        self.root.after(1000, self.check_alarm)

    def check_alarm(self):
        current_time = time.strftime("%H:%M:%S")
        current_seconds = self.convert_to_seconds(current_time)

        if current_seconds == self.alarm_seconds:
            self.ring_alarm()
        else:
            self.root.after(1000, self.check_alarm)

    def ring_alarm(self):
        messagebox.showinfo("Alarm", "Time to wake up!")
        
    def stop_alarm(self):
        self.alarm_time.set("")

    def convert_to_seconds(self, time_str):
        try:
            hours, minutes, seconds = map(int, time_str.split(":"))
            total_seconds = hours * 3600 + minutes * 60 + seconds
            return total_seconds
        except ValueError:
            return -1

def main():
    root = tk.Tk()
    app = AlarmClock(root)
    root.mainloop()

if __name__ == "__main__":
    main()
