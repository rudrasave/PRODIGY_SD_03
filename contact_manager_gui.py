import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

# File to store contacts
FILE_NAME = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save contacts to file
def save_contacts():
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

# Add contact
def add_contact():
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()

    if name == "" or phone == "" or email == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts()
    refresh_list()
    clear_entries()

# Refresh the listbox display
def refresh_list():
    listbox.delete(0, tk.END)
    for idx, contact in enumerate(contacts):
        listbox.insert(tk.END, f"{idx+1}. {contact['name']} - {contact['phone']} - {contact['email']}")

# Clear the entry fields
def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# Edit selected contact
def edit_contact():
    selected = listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Select a contact to edit.")
        return

    index = selected[0]
    contact = contacts[index]

    new_name = simpledialog.askstring("Edit Name", "Enter new name:", initialvalue=contact["name"])
    new_phone = simpledialog.askstring("Edit Phone", "Enter new phone:", initialvalue=contact["phone"])
    new_email = simpledialog.askstring("Edit Email", "Enter new email:", initialvalue=contact["email"])

    if new_name and new_phone and new_email:
        contacts[index] = {"name": new_name, "phone": new_phone, "email": new_email}
        save_contacts()
        refresh_list()

# Delete selected contact
def delete_contact():
    selected = listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Select a contact to delete.")
        return

    index = selected[0]
    confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this contact?")
    if confirm:
        contacts.pop(index)
        save_contacts()
        refresh_list()

# --- GUI Setup ---
root = tk.Tk()
root.title("Contact Manager")
root.geometry("500x500")

# Input Fields
tk.Label(root, text="Name:").pack()
entry_name = tk.Entry(root, width=40)
entry_name.pack()

tk.Label(root, text="Phone:").pack()
entry_phone = tk.Entry(root, width=40)
entry_phone.pack()

tk.Label(root, text="Email:").pack()
entry_email = tk.Entry(root, width=40)
entry_email.pack()

tk.Button(root, text="Add Contact", command=add_contact).pack(pady=10)

# Contact List
listbox = tk.Listbox(root, width=60, height=10)
listbox.pack(pady=10)

# Edit / Delete Buttons
tk.Button(root, text="Edit Selected Contact", command=edit_contact).pack(pady=5)
tk.Button(root, text="Delete Selected Contact", command=delete_contact).pack(pady=5)

# Load data and refresh display
contacts = load_contacts()
refresh_list()

root.mainloop()
