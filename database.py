
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
SELECT_USER = "SELECT * FROM users WHERE user.id = ?;"
SELECT_USER_CONTACTS = "SELECT * FROM contacts WHERE user_id = ?;"

INSERT_USER = "INSERT INTO users (name, email, password) VALUES (?, ?, ?);"
INSERT_CONTACT = "INSERT INTO contacts (name, phone_no, email, user_id) VALUES (?, ?, ?, ?);"


# -- DATABASE CONNECTION --
def create_tables(connection):
    """Create database tables"""
    with connection:
        cursor = connection.cursor()
        cursor.execute(CREATE_USERS)
        cursor.execute(CREATE_CONTACTS)


# -- USERS --
def create_user(connection, name: str, email: str, password: str):
    """Create new user & return id from database"""
    with connection:
        cursor = connection.cursor()
        cursor.execute(INSERT_USER, (name, email, password))
        user_id = cursor.lastrowid
        return user_id


# -- CONTACTS --
def add_contact(connection, contact_name: str, contact_phone_no: str, contact_email: str, user_id: int):
    """Create a new contact for specified user"""
    with connection:
        cursor = connection.cursor()
        cursor.execute(INSERT_CONTACT, (contact_name,
                                        contact_phone_no, contact_email, user_id))
        contact_id = cursor.lastrowid
        return contact_id
