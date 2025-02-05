# Contact class
class Contact:
    def __init__(self, name: str, phone_number: str, email: str):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone_number}, Email: {self.email}"


# Contact Manager class
class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact: Contact):
        self.contacts.append(contact)

    def remove_contact(self, name: str):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact '{name}' removed successfully.")
                return
        print("Contact not found.")

    def search_contact(self, name: str):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        print("Contact not found.")
        return None

    def list_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        sorted_contacts = sorted(self.contacts, key=lambda c: c.name.lower())
        for contact in sorted_contacts:
            print(contact)


# Factory function
def contact_factory(name: str, phone_number: str, email: str) -> Contact:
    return Contact(name, phone_number, email)


# Example usage
if __name__ == "__main__":
    manager = ContactManager()

    # Creating contacts using the factory function
    contact1 = contact_factory("Alice", "123-456-7890", "alice@example.com")
    contact2 = contact_factory("Bob", "987-654-3210", "bob@example.com")
    contact3 = contact_factory("Charlie", "555-666-7777", "charlie@example.com")

    # Adding contacts
    manager.add_contact(contact1)
    manager.add_contact(contact2)
    manager.add_contact(contact3)

    # Listing contacts
    print("\nList of Contacts:")
    manager.list_contacts()

    # Searching for a contact
    print("\nSearch for Bob:")
    found_contact = manager.search_contact("Bob")
    if found_contact:
        print(found_contact)

    # Removing a contact
    print("\nRemoving Alice:")
    manager.remove_contact("Alice")

    # Listing contacts after removal
    print("\nUpdated List of Contacts:")
    manager.list_contacts()
