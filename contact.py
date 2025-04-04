contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print("Contact added successfully!\n")
def view_contacts():
    if not contacts:
        print("No contacts to display.\n")
        return
    print("\nAll Contacts:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    print()
