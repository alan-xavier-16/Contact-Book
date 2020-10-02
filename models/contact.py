from connection import create_connection
from database import add_contact


class Contact:
    """Class to manage contacts"""

    def __init__(self, contact_name: str, contact_phone_no: str, contact_email: str, user_id: int, _id: int = None):
        self.id = _id
        self.name = contact_name
        self.phone_no = contact_phone_no
        self.email = contact_email
        self.user_id = user_id

    def __repr__(self) -> str:
        return f"Contact({self.name!r}, {self.phone_no!r}, {self.email!r}, {self.user_id!r}, {self.id!r})"

    def save(self):
        """Save contact to database"""
        with create_connection() as connection:
            new_contact_id = add_contact(
                connection, self.name, self.phone_no, self.email, self.user_id)
            self.id = new_contact_id
