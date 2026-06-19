
    contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone

    elif choice == "2":
        for name, phone in contacts.items():
            print(name, ":", phone)

    elif choice == "3":
        name = input("Enter name: ")
        print(contacts.get(name, "Not Found"))

    elif choice == "4":
        break