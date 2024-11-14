import tkinter as tk
from tkinter import messagebox

class AddressBook:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Address Book")
        self.window.geometry("400x300")

        self.addresses = []

        self.name_label = tk.Label(self.window, text="Name:")
        self.name_label.pack()

        self.name_entry = tk.Entry(self.window)
        self.name_entry.pack()

        self.address_label = tk.Label(self.window, text="Address:")
        self.address_label.pack()

        self.address_entry = tk.Text(self.window, height=5, width=30)
        self.address_entry.pack()

        self.add_button = tk.Button(self.window, text="Add", command=self.add_address)
        self.add_button.pack()

        self.view_button = tk.Button(self.window, text="View", command=self.view_addresses)
        self.view_button.pack()

        self.clear_button = tk.Button(self.window, text="Clear", command=self.clear_entries)
        self.clear_button.pack()

    def add_address(self):
        name = self.name_entry.get()
        address = self.address_entry.get("1.0", "end-1c")
        if name and address:
            self.addresses.append({"name": name, "address": address})
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please enter both name and address")

    def view_addresses(self):
        address_string = ""
        for address in self.addresses:
            address_string += "Name: " + address["name"] + "\nAddress: " + address["address"] + "\n\n"
        messagebox.showinfo("Addresses", address_string)

    def clear_entries(self):
        self.name_entry.delete(0, "end")
        self.address_entry.delete("1.0", "end")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    address_book = AddressBook()
    address_book.run()