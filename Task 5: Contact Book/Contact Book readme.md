# Contact Book

## Overview

The Contact Book Management System is a GUI-based desktop application developed using Python, Tkinter, and SQLite. The application allows users to efficiently manage their contacts by adding, searching, updating, viewing, and deleting contact information.

All contact data is stored permanently using an SQLite database, ensuring that information remains available even after closing the application.

---

## Features

### Add Contact

Users can add new contacts by entering:

* Name
* Phone Number
* Email Address
* Address

### View Contacts

Displays all saved contacts in a table format.

### Search Contact

Search contacts using:

* Name
* Phone Number

### Update Contact

Modify existing contact information.

### Delete Contact

Remove unwanted contacts from the database.

### Permanent Storage

Contacts are stored in an SQLite database (`contacts.db`) and remain available after restarting the application.

### Contact Counter

Displays the total number of saved contacts.

### User-Friendly Interface

Simple and intuitive graphical user interface built with Tkinter.

---

## Technologies Used

* Python 3
* Tkinter
* SQLite3

---

## Database Structure

### Table: contacts

| Column  | Type    |
| ------- | ------- |
| id      | INTEGER |
| name    | TEXT    |
| phone   | TEXT    |
| email   | TEXT    |
| address | TEXT    |

---

## How to Run

### Step 1: Install Python

Download and install Python from:

https://www.python.org/downloads/

### Step 2: Save the Source Code

Save the project as:

```text
contact_book.py
```

### Step 3: Run the Program

Open Terminal or Command Prompt and execute:

python contact_book.py


---

## Sample Usage

### Add Contact

Name    : Vraj Modi
Phone   : 9876543210
Email   : vraj@gmail.com
Address : Anand

### Search Contact

Search Keyword: Vraj

### Update Contact

Select a contact from the table and update the required information.

### Delete Contact

Select a contact and click the Delete Contact button.

---

## Learning Outcomes

This project demonstrates:

* Python GUI Development using Tkinter
* Database Integration using SQLite
* CRUD Operations

  * Create
  * Read
  * Update
  * Delete
* Event Handling
* User Interface Design
* Data Persistence

---

## Future Enhancements

* Dark Theme Interface
* Contact Photo Support
* Export Contacts to CSV
* Import Contacts from Excel
* Phone Number Validation
* Email Validation
* Backup and Restore Database

---


## Conclusion

The Contact Book Management System is a practical desktop application that simplifies contact management. It combines GUI development and database management to provide a complete solution for storing and organizing personal contact information efficiently.
