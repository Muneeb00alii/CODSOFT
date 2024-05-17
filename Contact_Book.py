class Contact_Book:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("\nEnter contact name: ")
        number = input("Enter contact number: ")
        email = input("Enter contact email (optional): ")
        address = input("Enter contact address (optional): ")
        self.contacts.append({"Name": name, "Number": number, "Email": email, "Address": address})
        print("\nContact added successfully!")

    def search_contact(self):
        search_name = input("\nEnter contact name to search: ")
        for contact in self.contacts:
            if contact["Name"] == search_name:
                print("\nContact found!")
                print(f"Name: {contact['Name']}")
                print(f"Number: {contact['Number']}")
                print(f"Email: {contact['Email']}")
                print(f"Address: {contact['Address']}")
                break
        else:
            print("\nContact not found!")

    def delete_contact(self):
        delete_name = input("\nEnter contact name to delete: ")
        for contact in self.contacts:
            if contact["Name"] == delete_name:
                self.contacts.remove(contact)
                print("\nContact deleted successfully!")
                break
        else:
            print("\nContact not found!")

    def update_contact(self):
        update_name = input("\nEnter contact name to update: ")
        for contact in self.contacts:
            if contact["Name"] == update_name:
                name = input("\nEnter new contact name: ")
                number = input("Enter new contact number: ")
                email = input("Enter new contact email (optional): ")
                address = input("Enter new contact address (optional): ")
                contact["Name"] = name
                contact["Number"] = number
                contact["Email"] = email
                contact["Address"] = address
                print("\nContact updated successfully!")
                break
        else:
            print("\nContact not found!")

    def display_contacts(self):
        if self.contacts:
            for contact in self.contacts:
                print("\nName:", contact["Name"])
                print("Number:", contact["Number"])
                print("Email:", contact["Email"])
                print("Address:", contact["Address"])
                print("-" * 30)
        else:
            print("\nNo contacts available!")


if __name__ == "__main__":
    contact_book = Contact_Book()
    while True:
        print("\nContact Book:")
        print("\n1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Update Contact")
        print("5. Display Contacts")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            contact_book.add_contact()
        elif choice == "2":
            contact_book.search_contact()
        elif choice == "3":
            contact_book.delete_contact()
        elif choice == "4":
            contact_book.update_contact()
        elif choice == "5":
            contact_book.display_contacts()
        elif choice == "6":
            break
        else:
            print("\nInvalid choice! Try again.")
            continue

    print("\nThanks for using the Contact Book!")