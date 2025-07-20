import json
import os

# File name to store contacts
FILENAME = "contacts.json"

# Load existing contacts or create an empty list
def load_contacts():
    if os.path.exists(FILENAME): 
        with open(FILENAME, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(FILENAME, 'w') as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print(" No contacts found.")
    else:
        for i, c in enumerate(contacts, start=1):
            print(f"\n Contact {i}")
            print(f"Name : {c['name']}")
            print(f"Phone: {c['phone']}")
            print(f"Email: {c['email']}")

# Search contact by name
def search_contact(contacts):
    search_name = input(" Enter name to search: ").lower()
    found = False
    for c in contacts:
        if c['name'].lower() == search_name:
            print(f"\n Name : {c['name']}")
            print(f"Phone: {c['phone']}")
            print(f"Email: {c['email']}")
            found = True
    if not found:
        print("Contact not found.")

# Delete a contact
def delete_contact(contacts):
    name = input(" Enter name of contact to delete: ").lower()
    initial_len = len(contacts)
    contacts[:] = [c for c in contacts if c['name'].lower() != name]
    if len(contacts) < initial_len:
        save_contacts(contacts)
        print("Contact deleted.")
    else:
        print("Contact not found.")

# Update a contact
def update_contact(contacts):
    name = input(" Enter name of contact to update: ").lower()
    for c in contacts:
        if c['name'].lower() == name:
            print("Leave blank to keep current value.")
            new_phone = input(f"New phone (current: {c['phone']}): ")
            new_email = input(f"New email (current: {c['email']}): ")
            if new_phone:
                c['phone'] = new_phone
            if new_email:
                c['email'] = new_email
            save_contacts(contacts)
            print("Contact updated.")
            return
    print(" Contact not found.")

# Main menu loop
def menu():
    contacts = load_contacts()

    while True:
        print("\n====== Contact Book ======")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            update_contact(contacts)
        elif choice == '6':
            print(" Exiting Contact Book. Goodbye!")
            break
        else:
            print(" Invalid choice. Please select between 1 to 6.")

# Run the program
if __name__ == "__main__":
    menu()

