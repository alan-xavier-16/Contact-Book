from connection import create_connection
from models.contact import Contact
from database import create_user


class User:
    """Manages User's functionality"""

    def __init__(self, name: str, email: str, password: str, _id: int = None):
        self.id = _id
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self) -> str:
        return f"User({self.name!r}, {self.email!r}, {self.password!r}, {self.id!r})"

    def save(self):
        """Save user to database"""
        with create_connection() as connection:
            new_user_id = create_user(
                connection, self.name, self.email, self.password)
            self.id = new_user_id

    def add_contact(self, contact_name: str, contact_phone_no: int, contact_email: str):
        """Add new contact to database"""
        Contact(contact_name, contact_phone_no, contact_email, self.id)
