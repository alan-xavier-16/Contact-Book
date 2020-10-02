from typing import List, Tuple

# -- DATABASE TYPES
User = Tuple[int, str, str, str]
Contact = Tuple[int, str, str, str, int]

# -- DATABASE QUERIES --
CREATE_USERS = """CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY,
  name TEXT, 
  email TEXT, 
  password TEXT
);"""
CREATE_CONTACTS = """CREATE TABLE IF NOT EXISTS contacts (
  id INTEGER PRIMARY KEY,
  name TEXT,
  phone_no TEXT,
  email TEXT,
  user_id INTEGER,
  FOREIGN KEY(user_id) REFERENCES users(id)
);"""

SELECT_ALL_USERS = "SELECT * FROM users;"
SELECT_USER = "SELECT * FROM users WHERE id = ?;"
SELECT_USER_CONTACTS = "SELECT * FROM contacts WHERE user_id = ?;"
SELECT_CONTACT = "SELECT * FROM contacts WHERE id = ?;"

INSERT_USER = "INSERT INTO users (name, email, password) VALUES (?, ?, ?);"
INSERT_CONTACT = "INSERT INTO contacts (name, phone_no, email, user_id) VALUES (?, ?, ?, ?);"

UPDATE_USER = """UPDATE users 
SET name = ?, 
    email = ?,
    password = ?
WHERE id = ?;"""
UPDATE_CONTACT = """UPDATE contacts 
SET name = ?,
    phone_no = ?,
    email = ?
WHERE id = ? AND user_id = ?;"""

DELETE_USER = "DELETE FROM users WHERE id = ?;"
DELETE_USER_CONTACTS = "DELETE FROM contacts where user_id = ?;"
DELETE_CONTACT = "DELETE FROM contacts where id = ?;"


# -- DATABASE CONNECTION --
def create_tables(connection):
    """Create database tables"""
    with connection:
        cursor = connection.cursor()
        cursor.execute(CREATE_USERS)
        cursor.execute(CREATE_CONTACTS)


# -- USERS --
def get_users(connection) -> List[User]:
    """Returns users from database"""
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_ALL_USERS)
        return cursor.fetchall()


def get_user(connection, id: int) -> User:
    """Return a User from database"""
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_USER, (id,))
        return cursor.fetchone()


def create_user(connection, name: str, email: str, password: str):
    """Create new user & return id from database"""
    with connection:
        cursor = connection.cursor()
        cursor.execute(INSERT_USER, (name, email, password))
        user_id = cursor.lastrowid
        return user_id


def update_user(connection, name: str, email: str, password: str, user_id: int):
    """Update specified user in database"""
    with connection:
        cursor = connection.cursor()
        cursor.execute(UPDATE_USER, (name, email, password, user_id))
        return cursor.fetchone()


# -- CONTACTS --
def get_contacts(connection, user_id: int) -> List[Contact]:
    """Get ALL contact for a specified user"""
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_USER_CONTACTS, (user_id,))
        return cursor.fetchall()


def get_contact(connection, contact_id) -> Contact:
    """Get contact for user"""
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_CONTACT, (contact_id,))
        return cursor.fetchone()


def add_contact(connection, contact_name: str, contact_phone_no: str, contact_email: str, user_id: int):
    """Create a new contact for specified user"""
    with connection:
        cursor = connection.cursor()
        cursor.execute(INSERT_CONTACT, (contact_name,
                                        contact_phone_no, contact_email, user_id))
        contact_id = cursor.lastrowid
        return contact_id


def update_contact(connection, contact_name: str, contact_phone_no: str, contact_email: str, contact_id: int, user_id: int):
    """Update specified contact in database"""
    with connection:
        cursor = connection.cursor()
        cursor.execute(UPDATE_CONTACT, (contact_name,
                                        contact_phone_no, contact_email, contact_id, user_id))
        return cursor.fetchone()
