from connection import create_connection
from database import create_tables

from models.user import User
from models.contact import Contact

# -- MENU PROMPTS --
MENU_PROMPT = """--- MENU ---

1. Create user account.
2. Show all users.
3. Show a user.
4. Add new contact.
5. Show all contacts.
6. Show a contact.
7. Update user.
8. Update contact.
9. Delete user.
10. Delete contact.
11. Exit.

Enter your choice: """

NEW_CONTACT_PROMPT = "Enter new contact (or leave empty to exit): "


# -- MENU FUNCTIONS --
def prompt_create_user():
    """Create a new user"""
    name = input("Please enter name: ")
    email = input("Please enter email: ")
    password = input("Please enter password: ")
    new_user = User(name, email, password)
    new_user.save()


def show_all_users():
    """Show all users"""
    users = User.all()
    for user in users:
        print(user.__str__())
    print("\n")


def show_user():
    """Show a user"""
    user_id = int(input("Enter user id: "))
    user = User.get(user_id)
    print(user.__str__())
    print("\n")


def prompt_add_new_contact():
    """Add a new contact for user"""
    user_id = int(input("Please enter your user id: "))
    contact_name = input("Please enter contact name: ")
    contact_phone_num = input("Please enter contact phone no: ")
    contact_email = input("Please enter contact email: ")
    new_contact = Contact(contact_name, contact_phone_num,
                          contact_email, user_id)
    new_contact.save()


def show_all_contacts():
    """Show all contacts"""
    user_id = int(input("Please enter your user id: "))
    contacts = User.get(user_id).contacts
    for contact in contacts:
        print(contact.__str__())
    print("\n")


def show_contact():
    """Show a contact"""
    contact_id = int(input("Please enter contact id: "))
    contact = Contact.get(contact_id)
    print(contact.__str__())
    print("\n")


def update_user():
    """Update a user"""
    user_id = int(input("Please enter your user id: "))
    user = User.get(user_id)
    print(f"Current details: {user.__str__()}")

    if name := input("Please enter name: "):
        user.name = name
    if email := input("Please enter email: "):
        user.email = email
    if password := input("Please enter password: "):
        user.password = password

    user.update()
    print(f"New details: {user.__str__()}")


def update_contact():
    """Update a contact"""
    contact_id = int(input("Please enter contact id: "))
    contact = Contact.get(contact_id)
    print(f"Current details: {contact.__str__()}")

    if contact_name := input("Please enter contact name: "):
        contact.name = contact_name
    if contact_phone_num := input("Please enter contact phone no: "):
        contact.phone_no = contact_phone_num
    if contact_email := input("Please enter contact email: "):
        contact.email = contact_email

    contact.update()
    print(f"New details: {contact.__str__()}")


def delete_user():
    """Remove a user"""
    user_id = int(input("Please enter your user id: "))
    User.remove(user_id)
    print(f"User removed")


def delete_contact():
    """Remove a contact"""
    contact_id = int(input("Please enter contact id: "))
    Contact.remove(contact_id)
    print(f"Contact removed")


# -- USER INTERFACE --
MENU_OPTIONS = {
    "1": prompt_create_user,
    "2": show_all_users,
    "3": show_user,
    "4": prompt_add_new_contact,
    "5": show_all_contacts,
    "6": show_contact,
    "7": update_user,
    "8": update_contact,
    "9": delete_user,
    "10": delete_contact
}


def menu():
    """Contact Book User Interface"""
    with create_connection() as connection:
        create_tables(connection)

    while (selection := input(MENU_PROMPT)) != "11":
        try:
            MENU_OPTIONS[selection]()
        except KeyError:
            print("Invalid selection, please try again.\n")


if(__name__ == "__main__"):
    menu()
