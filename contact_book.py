import json
import os

filename = "contacts.json"

def load_contacts():
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    with open(filename, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    phone = input("Enter contact phone number: ").strip()
    email = input("Enter contact email: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"Contact {name} added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

def search_contact(contacts):
    name = input("Enter contact name to search: ").strip()
    if name in contacts:
        print(f"Name: {name}, Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
    else:
        print(f"Contact {name} not found.")

def delete_contact(contacts):
    name = input("Enter contact name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact {name}deleted successfully.")
    else:
        print(f"Contact {name} not found.")

def menu():
    contacts = load_contacts()
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

menu()
          

