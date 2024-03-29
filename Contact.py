class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contact = Contact(name, phone, email, address)
        self.contacts[name] = contact
        print("Contact added successfully!")

    def view_contact_list(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contact List:")
            for contact in self.contacts.values():
                print(f"Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self):
        search_term = input("Enter name or phone number to search: ")
        found = False
        for contact in self.contacts.values():
            if search_term in [contact.name, contact.phone]:
                print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")
                found = True
        if not found:
            print("Contact not found.")

    def update_contact(self):
        name = input("Enter the name of the contact to update: ")
        if name in self.contacts:
            contact = self.contacts[name]
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            contact.phone = phone
            contact.email = email
            contact.address = address
            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    def delete_contact(self):
        name = input("Enter the name of the contact to delete: ")
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

contact_manager = ContactManager()

while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        contact_manager.add_contact()
    elif choice == '2':
        contact_manager.view_contact_list()
    elif choice == '3':
        contact_manager.search_contact()
    elif choice == '4':
        contact_manager.update_contact()
    elif choice == '5':
        contact_manager.delete_contact()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")
