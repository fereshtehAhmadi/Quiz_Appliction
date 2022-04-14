from .validator import (
    validate_username,
    validate_password,
    match_password,
    validate_city,
    validate_emaill,
)
from .hide_password import secure_password_input
import termcolor2
import bcrypt
import hashlib
import sqlite3


def get_login_data():
    while True:
        username = input('Enter your username: ')
        if not username:
            
            print(termcolor2.colored('Empty username is not allowed', color="red"))
            continue

        password = secure_password_input(prompt="Enter password: ")
        if not password:
            print(termcolor2.colored('Empty password is not allowed'))
            continue

        break

    return username, password


def get_register_data():
    while True:
        username = input('Enter your username: ')
        if not validate_username(username): continue

        password = secure_password_input(prompt="Enter password: ")
        if not validate_password(password): continue

        confirm_password = secure_password_input(prompt="Enter password: ")
        if not match_password(password, confirm_password): continue

        fname = input('Enter your first name: ')
        if not validate_city(fname): continue

        lname = input('Enter your last name: ')
        if not validate_city(lname): continue

        city = input('Enter your city: ')
        if not validate_city(city): continue

        email = input('Enter your email: ')
        if not validate_emaill(email): continue

        break

    return username, password, fname, lname, city, email