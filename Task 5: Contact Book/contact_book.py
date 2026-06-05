import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# ---------------- DATABASE ---------------- #

conn = sqlite3.connect("contacts.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT,
    address TEXT
)
""")

conn.commit()

# ---------------- FUNCTIONS ---------------- #

def clear_fields():
    name_var.set("")
    phone_var.set("")
    email_var.set("")
    address_var.set("")


def show_contacts():
    contact_table.delete(*contact_table.get_children())

    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()

    for row in rows:
        contact_table.insert(
            "",
            tk.END,
            values=row
        )

    total_label.config(
        text=f"Total Contacts: {len(rows)}"
    )


def add_contact():
    name = name_var.get()
    phone = phone_var.get()
    email = email_var.get()
    address = address_var.get()

    if name == "" or phone == "":
        messagebox.showerror(
            "Error",
            "Name and Phone are required!"
        )
        return

    cursor.execute("""
    INSERT INTO contacts(name, phone, email, address)
    VALUES(?,?,?,?)
    """, (name, phone, email, address))

    conn.commit()

    show_contacts()
    clear_fields()

    messagebox.showinfo(
        "Success",
        "Contact Added Successfully!"
    )


def select_contact(event):
    selected = contact_table.focus()

    if selected:
        values = contact_table.item(selected, "values")

        name_var.set(values[1])
        phone_var.set(values[2])
        email_var.set(values[3])
        address_var.set(values[4])


def update_contact():
    selected = contact_table.focus()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Select a contact first!"
        )
        return

    contact_id = contact_table.item(selected)["values"][0]

    cursor.execute("""
    UPDATE contacts
    SET name=?, phone=?, email=?, address=?
    WHERE id=?
    """,
    (
        name_var.get(),
        phone_var.get(),
        email_var.get(),
        address_var.get(),
        contact_id
    ))

    conn.commit()

    show_contacts()
    clear_fields()

    messagebox.showinfo(
        "Updated",
        "Contact Updated Successfully!"
    )


def delete_contact():
    selected = contact_table.focus()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Select a contact first!"
        )
        return

    contact_id = contact_table.item(selected)["values"][0]

    confirm = messagebox.askyesno(
        "Delete Contact",
        "Are you sure you want to delete this contact?"
    )

    if confirm:
        cursor.execute(
            "DELETE FROM contacts WHERE id=?",
            (contact_id,)
        )

        conn.commit()

        show_contacts()
        clear_fields()

        messagebox.showinfo(
            "Deleted",
            "Contact Deleted Successfully!"
        )


def search_contact():
    keyword = search_var.get()

    contact_table.delete(*contact_table.get_children())

    cursor.execute("""
    SELECT * FROM contacts
    WHERE name LIKE ? OR phone LIKE ?
    """,
    (
        "%" + keyword + "%",
        "%" + keyword + "%"
    ))

    rows = cursor.fetchall()

    for row in rows:
        contact_table.insert(
            "",
            tk.END,
            values=row
        )

# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Contact Book Management System")
root.geometry("950x600")
root.resizable(False, False)
root.configure(bg="#f5f5f5")

title = tk.Label(
    root,
    text="CONTACT BOOK MANAGEMENT SYSTEM",
    font=("Arial", 18, "bold"),
    bg="#f5f5f5"
)
title.pack(pady=10)

# Variables

name_var = tk.StringVar()
phone_var = tk.StringVar()
email_var = tk.StringVar()
address_var = tk.StringVar()
search_var = tk.StringVar()

# Input Frame

frame = tk.Frame(root, bg="#f5f5f5")
frame.pack(pady=10)

tk.Label(frame, text="Name", bg="#f5f5f5").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(frame, textvariable=name_var, width=30).grid(row=0, column=1)

tk.Label(frame, text="Phone", bg="#f5f5f5").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(frame, textvariable=phone_var, width=30).grid(row=1, column=1)

tk.Label(frame, text="Email", bg="#f5f5f5").grid(row=0, column=2, padx=5, pady=5)
tk.Entry(frame, textvariable=email_var, width=30).grid(row=0, column=3)

tk.Label(frame, text="Address", bg="#f5f5f5").grid(row=1, column=2, padx=5, pady=5)
tk.Entry(frame, textvariable=address_var, width=30).grid(row=1, column=3)

# Buttons

button_frame = tk.Frame(root, bg="#f5f5f5")
button_frame.pack(pady=10)

tk.Button(
    button_frame,
    text="Add Contact",
    width=15,
    command=add_contact
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text="Update Contact",
    width=15,
    command=update_contact
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame,
    text="Delete Contact",
    width=15,
    command=delete_contact
).grid(row=0, column=2, padx=5)

tk.Button(
    button_frame,
    text="Clear",
    width=15,
    command=clear_fields
).grid(row=0, column=3, padx=5)

# Search

search_frame = tk.Frame(root, bg="#f5f5f5")
search_frame.pack(pady=10)

tk.Entry(
    search_frame,
    textvariable=search_var,
    width=30
).grid(row=0, column=0, padx=5)

tk.Button(
    search_frame,
    text="Search",
    command=search_contact
).grid(row=0, column=1, padx=5)

tk.Button(
    search_frame,
    text="Show All",
    command=show_contacts
).grid(row=0, column=2, padx=5)

# Table

columns = (
    "ID",
    "Name",
    "Phone",
    "Email",
    "Address"
)

contact_table = ttk.Treeview(
    root,
    columns=columns,
    show="headings",
    height=15
)

for col in columns:
    contact_table.heading(col, text=col)

contact_table.column("ID", width=50)
contact_table.column("Name", width=150)
contact_table.column("Phone", width=150)
contact_table.column("Email", width=220)
contact_table.column("Address", width=300)

contact_table.pack(fill="both", padx=10)

contact_table.bind(
    "<ButtonRelease-1>",
    select_contact
)

# Footer

total_label = tk.Label(
    root,
    text="Total Contacts: 0",
    font=("Arial", 11, "bold"),
    bg="#f5f5f5"
)

total_label.pack(pady=10)

# Load existing contacts on startup
show_contacts()

root.mainloop()

# Close database connection
conn.close()