import os
from dotenv import load_dotenv
import mysql.connector as mycon

from utils import hash_password

load_dotenv()

DB_HOST = os.getenv("HOST")
DB_USER = os.getenv("USER")
DB_PASSWORD = os.getenv("PASSWORD")
DB_DATABASE = os.getenv("DATABASE")

__cnx = None


def get_connection():
    global __cnx
    if not __cnx:
        try:
            __cnx = mycon.connect(
                host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_DATABASE
            )
        except Exception as er:
            print(er)

    return __cnx


## Books functions


def get_books():
    cnn = get_connection()
    cur = cnn.cursor()

    QUERY = "SELECT * FROM books"

    try:
        cur.execute(QUERY)
    except Exception as er:
        print(f"[ERROR] - {er}")

    data = cur.fetchall()

    if data:
        return data


def add_book_db(title, author, genre_id, description, total_amount):
    cnn = get_connection()
    cur = cnn.cursor()

    QUERY = "INSERT INTO books (title, author, genre_id, description, total_amount) VALUES (%s, %s, %s, %s, %s)"
    VALUES = (title, author, genre_id, description, total_amount)

    try:
        cur.execute(QUERY, VALUES)
        print(f"[SUCCESS] - Added book {title} by {author}")
    except Exception as er:
        print(f"[ERROR] - {er}")

    cnn.commit()


def update_book_db(book_id, field, new_value):
    cnn = get_connection()
    cur = cnn.cursor()

    QUERY = f"UPDATE books SET {field} = %s WHERE id = %s"
    VALUES = (new_value, book_id)

    try:
        cur.execute(QUERY, VALUES)
        print(f"[SUCCESS] - Updated book ID {book_id}, set {field} to {new_value}")
    except Exception as er:
        print(f"[ERROR] - {er}")

    cnn.commit()

def get_book_id(title):
    cnn = get_connection()
    cur = cnn.cursor()

    QUERY = "SELECT * FROM books WHERE title=%s"
    VALUES = (title,)

    try:
        cur.execute(QUERY, VALUES)
    except Exception as er:
        print(f"[ERROR] - {er}")

    data = cur.fetchone()

    if data:
        return data[0]

def get_book_from_id(book_id):
    cnn = get_connection()
    cur = cnn.cursor()

    QUERY = "SELECT * FROM books WHERE id=%s"
    VALUES = (book_id,)

    try:
        cur.execute(QUERY, VALUES)
    except Exception as er:
        print(f"[ERROR] - {er}")

    data = cur.fetchone()

    if data:
        return data

## Admin fucntions


def get_users(user_type="Student"):
    cnn = get_connection()
    cur = cnn.cursor()

    QUERY = "SELECT * FROM users WHERE role_id=%s"
    VALUES = (get_role_id(user_type),)

    try:
        cur.execute(QUERY, VALUES)
    except Exception as er:
        print(f"[ERROR] - {er}")

    data = cur.fetchall()

    if data:
        return data


def get_user(email, role="Student"):
    cnn = get_connection()
    cur = cnn.cursor()

    QUERY = "SELECT * FROM users WHERE email=%s AND role_id=%s"
    VALUES = (email, get_role_id(role))

    try:
        cur.execute(QUERY, VALUES)
    except Exception as er:
        print(f"[ERROR] - {er}")

    data = cur.fetchone()

    if data:
        return data


def get_user_from_id(user_id):
    cnn = get_connection()
    cur = cnn.cursor()

    QUERY = "SELECT * FROM users WHERE id=%s"
    VALUES = (user_id,)

    try:
        cur.execute(QUERY, VALUES)
    except Exception as er:
        print(f"[ERROR] - {er}")

    data = cur.fetchone()

    if data:
        return data

def add_user_db(firstname, surname, email, mobile_phone, password, gender_id, address, role_id):
    cnn = get_connection()
    cur = cnn.cursor()

    QUERY = "INSERT INTO users (firstname, surname, email, mobile_phone, password_hash, gender_id, address, role_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    VALUES = (firstname,surname,email,mobile_phone,hash_password(password),gender_id,address,role_id)

    try:
        cur.execute(QUERY, VALUES)
        print(f"[SUCCESS] - Added user {firstname} {surname}")
    except Exception as er:
        print(f"[ERROR] - {er}")

    cnn.commit()


def update_user_db(user_id, field, new_value):
    cnn = get_connection()
    cur = cnn.cursor()

    QUERY = f"UPDATE users SET {field} = %s WHERE id = %s"
    VALUES = (new_value, user_id)

    try:
        cur.execute(QUERY, VALUES)
        print(f"[SUCCESS] - Updated user ID {user_id}, set {field} to {new_value}")
    except Exception as er:
        print(f"[ERROR] - {er}")

    cnn.commit()

## Gender functions
def get_gender_id(gender):
    cnn = get_connection()
    cur = cnn.cursor()

    QUERY = "SELECT * from gender WHERE type=%s"
    VALUES = (gender,)

    try:
        cur.execute(QUERY, VALUES)
    except Exception as er:
        print(f"[ERROR] - {er}")

    data = cur.fetchone()

    if data:
        return data[0]


## Role functions
def get_role_id(role):
    cnn = get_connection()
    cur = cnn.cursor()

    QUERY = "SELECT * from role WHERE type=%s"
    VALUES = (role,)

    try:
        cur.execute(QUERY, VALUES)
    except Exception as er:
        print(f"[ERROR] - {er}")

    data = cur.fetchone()

    if data:
        return data[0]


def get_role_name(role_id):
    cnn = get_connection()
    cur = cnn.cursor()

    QUERY = "SELECT * from role WHERE id=%s"
    VALUES = (role_id,)

    try:
        cur.execute(QUERY, VALUES)
    except Exception as er:
        print(f"[ERROR] - {er}")

    data = cur.fetchone()

    if data:
        return data[1]


## Genre functions
def get_genre_id(genre):
    cnn = get_connection()
    cur = cnn.cursor()

    QUERY = "SELECT * from genre WHERE type=%s"
    VALUES = (genre,)

    try:
        cur.execute(QUERY, VALUES)
    except Exception as er:
        print(f"[ERROR] - {er}")

    data = cur.fetchone()

    if data:
        return data[0]


def get_genre_name(genre_id):
    cnn = get_connection()
    cur = cnn.cursor()

    QUERY = "SELECT * from genre WHERE id=%s"
    VALUES = (genre_id,)

    try:
        cur.execute(QUERY, VALUES)
    except Exception as er:
        print(f"[ERROR] - {er}")

    data = cur.fetchone()

    if data:
        return data[1]


## Events functions


def issue_book(book_id, user_id):
    cnn = get_connection()
    cur = cnn.cursor()

    QUERY = (
        "INSERT INTO events (book_id, user_id, issue_date) VALUES (%s, %s, CURDATE())"
    )
    VALUES = (book_id, user_id)

    try:
        cur.execute(QUERY, VALUES)
        print(f"[SUCCESS] - Issued book {book_id} to user {user_id}")
    except Exception as er:
        print(f"[ERROR] - {er}")

    cnn.commit()


def return_book(book_id, user_id):
    cnn = get_connection()
    cur = cnn.cursor()

    QUERY = "UPDATE events SET return_date=CURDATE() WHERE book_id=%s AND user_id=%s AND return_date IS NULL"
    VALUES = (book_id, user_id)

    try:
        cur.execute(QUERY, VALUES)
        print(f"[SUCCESS] - Returned book {book_id} from user {user_id}")
    except Exception as er:
        print(f"[ERROR] - {er}")

    cnn.commit()

def get_issued_books():
    cnn = get_connection()
    cur = cnn.cursor()

    QUERY = "SELECT * FROM events"

    try:
        cur.execute(QUERY)
    except Exception as er:
        print(f"[ERROR] - {er}")

    data = cur.fetchall()

    if data:
        return data
    