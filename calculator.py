import tkinter as tk
from tkinter import messagebox
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.create_widgets()
    def create_widgets(self):
        self.entry = tk.Entry(self.root, width=16, font=('Arial', 24), borderwidth=2, relief='solid')
        self.entry.grid(row=0, column=0, columnspan=4)
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            if button == '=':
                tk.Button(self.root, text=button, width=10, height=3, command=self.calculate).grid(row=row_val,
                                                                                                   column=col_val,
                                                                                                   columnspan=2)
                col_val += 1
            else:
                tk.Button(self.root, text=button, width=5, height=3,
                          command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        tk.Button(self.root, text='C', width=5, height=3, command=self.clear).grid(row=row_val, column=col_val)

    def on_button_click(self, char):
        current_text = self.entry.get()
        new_text = current_text + char
        self.entry.delete(0, tk.END)
        self.entry.insert(0, new_text)

    def calculate(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, result)
        except Exception as e:
            messagebox.showerror("Error", f"Invalid Input: {e}")
            self.clear()

    def clear(self):
        self.entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
