import time
from prettytable import PrettyTable
from datetime import datetime
import os

from database import (
    get_users, 
    get_user,
    add_user_db, 
    add_book_db, 
    get_books,
    get_gender_id, 
    get_role_id, 
    get_genre_id, 
    get_genre_name, 
    get_role_name, 
    issue_book, 
    get_book_id, 
    return_book, 
    get_issued_books, 
    get_user_from_id, 
    get_book_from_id, 
    update_book_db, 
    update_user_db, 
    get_genres
    )
from utils import verify_password, clear_screen

if not os.path.exists(".env"):
    print("Config file not found!")
    exit(1)

def add_user_cli(role="Student"):
    firstname = input("Enter your first name : ")
    surname = input("Enter your surname : ")
    email = input("Enter your email : ")
    mobile_phone = input("Enter your mobile number : (+91) ")
    gender = input("Select your gender : ")
    while not get_gender_id(gender):
        gender = input("Please select valid gender : ")
    address = input("Enter your address : ")

    if role == "Admin":
        password = input("Select a strong password : ")
        confirm_password = input("Confirm your password : ")

        while password != confirm_password:
            confirm_password = input("Please enter correct password : ")

        add_user_db(firstname,surname,email,mobile_phone,password,get_gender_id(gender),address,get_role_id(role))
    else:
        add_user_db(firstname,surname,email,mobile_phone,None,get_gender_id(gender),address,get_role_id(role))


def update_user_cli():
    email = input("Enter the email of the user : ")
    field = input("Enter the field to update : ")
    new_value = input("Enter the new value : ")

    if get_user(email):
        update_user_db(get_user(email)[0], field, new_value)
    else:
        print("[ERROR] - User not found")


def display_users_cli():
    users = get_users()

    if users:
        table = PrettyTable()
        table.field_names = ["ID", "Name", "Email", "Role"]

        for user in users:
            table.add_row(
                [user[0], f"{user[1]} {user[2]}", user[3], get_role_name(user[8])]
            )

        print(table)
    else:
        print("[INFO] - No users found")


def users_menu():
    print("          Users Menu            ")
    print("          ----------            ")
    while True:
        print("1. Add User")
        print("2. Update User")
        print("3. Display Users")
        print("4. Back")

        choice = input("Enter your choice : ")

        if choice == "1":
            add_user_cli()
        elif choice == "2":
            update_user_cli()
        elif choice == "3":
            display_users_cli()
        elif choice == "4":
            break
        else:
            print("Invalid choice")


def add_book_cli():
    title = input("Enter the title of the book : ")
    author = input("Enter the author of the book : ")
    genre = input("Enter the genre of the book : ")
    while not get_genre_id(genre):
        genre = input("Please select valid genre : ")
    description = input("Enter the description of the book : ")
    total_amount = input("Enter the total amount of the book : ")

    add_book_db(title, author, get_genre_id(genre), description, total_amount)


def update_book_cli():
    title = input("Enter the title of the book : ")
    field = input("Enter the field to update : ")
    new_value = input("Enter the new value : ")

    if get_book_id(title):
        update_book_db(get_book_id(title), field, new_value)
    else:
        print("[ERROR] - Book not found")


def display_books_cli():
    books = get_books()

    if books:

        table = PrettyTable()
        table.field_names = ["ID","Title","Author","Genre","Description","Total Amount"]

        for book in books:
            table.add_row([book[0], book[1], book[2], get_genre_name(book[3]), book[4], book[5]])

        print(table)
    else:
        print("[INFO] - No books found")


def show_genres_cli():
    genres = get_genres()

    if genres:
        table = PrettyTable()
        table.field_names = ["ID", "Genre"]

        for genre in genres:
            table.add_row([genre[0], genre[1]])

        print(table)
    else:
        print("[INFO] - No genres found")

def books_menu():
    print("          Books Menu            ")
    print("          ----------            ")
    while True:
        print("1. Add Book")
        print("2. Update Book")
        print("3. Display Books")
        print("4. Show Genres")
        print("5. Back")

        choice = input("Enter your choice : ")

        if choice == "1":
            add_book_cli()
        elif choice == "2":
            update_book_cli()
        elif choice == "3":
            display_books_cli()
        elif choice == "4":
            show_genres_cli()
        elif choice == "5":
            break
        else:
            print("Invalid choice")


def issue_book_cli():
    email = input("Enter the email of the user : ")
    title = input("Enter the title of the book : ")

    if get_user(email):
        if get_book_id(title):
            issue_book(get_book_id(title), get_user(email)[0])
        else:
            print("[ERROR] - Book not found")
    else:
        print("[ERROR] - User not found")


def return_book_cli():
    email = input("Enter the email of the user : ")
    title = input("Enter the title of the book : ")

    if get_user(email):
        if get_book_id(title):
            return_book(get_book_id(title), get_user(email)[0])
        else:
            print("[ERROR] - Book not found")
    else:
        print("[ERROR] - User not found")


def get_issued_books_cli():
    books = get_issued_books()

    if books:
        table = PrettyTable()
        table.field_names = ["ID", "Book", "User", "Issued Date", "Return Date"]

        for book in books:
            user = get_user_from_id(book[2])
            table.add_row([book[0],get_book_from_id(book[1])[1],f"{user[1]} {user[2]}",book[3],book[4],])

        print(table)
    else:
        print("[INFO] - No transaction found")


def issue_return_menu():
    print("          Issue/Return Menu            ")
    print("          -----------------            ")
    while True:
        print("1. Issue Book")
        print("2. Return Book")
        print("3. Display Issued Books")
        print("4. Back")

        choice = input("Enter your choice : ")

        if choice == "1":
            issue_book_cli()
        elif choice == "2":
            return_book_cli()
        elif choice == "3":
            get_issued_books_cli()
        elif choice == "4":
            break
        else:
            print("Invalid choice")


def dashboard():
    while True:
        clear_screen()
        print("          Welcome to LMS - Library Management System            ")
        print("          -----------------------------------------            ")
        print("1. Users Menu")
        print("2. Books Menu")
        print("3. Issue/Return")
        print("4. Exit")

        choice = input("Enter your choice : ")

        if choice == "1":
            clear_screen()
            users_menu()
        elif choice == "2":
            clear_screen()
            books_menu()
        elif choice == "3":
            clear_screen()
            issue_return_menu()
        elif choice == "4":
            clear_screen()
            break
        else:
            print("Invalid choice")


def login():
    email = input("Enter your email : ")
    password = input("Enter your password : ")

    user = get_user(email, role="Admin")

    if user:
        if verify_password(password, user[5]):
            print("[SUCCESS] - Login successful")
            time.sleep(1)
            clear_screen()
            dashboard()
        else:
            print("[ERROR] - Incorrect password")
    else:
        print("[ERROR] - Admin not found")


def main():
    clear_screen()
    while True:
        if not get_users("Admin"):
            print("Please add an admin to continue")
            add_user_cli("Admin")
            time.sleep(1)
            clear_screen()
        print("Please Login to continue")
        login()


if __name__ == "__main__":
    main()
