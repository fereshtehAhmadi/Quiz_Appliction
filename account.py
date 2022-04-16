# from users import users_list, add_user_to_file, get_user_by_username
import bcrypt
from users import add_user_to_file
from logger import log_user_register
from datetime import datetime
from users import get_user_by_username, get_users
import termcolor2


def register(username, password, fname, lname, city, email):  
    add_user_to_file(username, password, fname, lname, city, email)
    log_user_register(username, datetime.now().replace(microsecond=0))
    


def login(username, password):
    users = get_users()

    if not users.get(username):
        print(termcolor2.colored(f'"{username}" does not exist!', color="red"))
        return False

    user_password = bytes(users.get(username).get('password'), 'utf-8')

    if username in users:
        if bcrypt.checkpw(bytes(password, 'utf-8'), user_password):
            print(termcolor2.colored(f'\n{username} Logged in successfully. ', color="green"))
            return True

    print(termcolor2.colored('Invalid credentials. ', color="red"))
        
