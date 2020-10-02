from sqlite3.dbapi2 import connect
from connection import create_connection
from database import create_tables

from models.user import User
from models.contact import Contact

# -- MENU PROMPTS --
MENU_PROMPT = """--- MENU ---

1. Create user account.
2. Show all users.
3. Add new contact.
4. Show all contact.
5. Exit.

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
    pass


def prompt_add_new_contact():
    """Add a new contact for user"""
    user_id = int(input("Please enter your user id: "))
    contact_name = input("Please enter contact name: ")
    contact_phone_num = input("Please enter contact phone no: ")
    contact_email = input("Please enter contact email: ")
    new_contact = Contact(contact_name, contact_phone_num,
                          contact_email, user_id)
    new_contact.save()


# -- USER INTERFACE --
MENU_OPTIONS = {
    "1": prompt_create_user,
    "2": show_all_users,
    "3": prompt_add_new_contact,
    "4": None
}


def menu():
    """Contact Book User Interface"""
    with create_connection() as connection:
        create_tables(connection)

    while (selection := input(MENU_PROMPT)) != "5":
        try:
            MENU_OPTIONS[selection]()
        except KeyError:
            print("Invalid selection, please try again.\n")


if(__name__ == "__main__"):
    menu()
