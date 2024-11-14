import tkinter as tk

def left_click(event):
    message_label.config(text="Left mouse button clicked!")

root = tk.Tk()
root.title("Left Mouse Button Message")

message_label = tk.Label(root, text="", font=("Arial", 14))
message_label.pack(pady=20)

# Bind left mouse button click event
root.bind("<Button-1>", left_click)

root.mainloop()
