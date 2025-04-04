contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print("Contact added successfully!\n")

