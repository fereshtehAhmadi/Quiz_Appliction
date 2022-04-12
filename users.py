from tabulate import tabulate
from prettytable import PrettyTable
import bcrypt
import hashlib


def get_users():
    handler = open('user.txt', 'r')
    file_raw_data = handler.read()
    users_list = file_raw_data.split('@@@')
    users_list.pop()
    users_dict = {}
    for usr in users_list:
        keys = ['password', 'first_name', 'last_name', 'email', 'city',]
        values = usr.split('??')
        user_username = values.pop(0)
        users_dict[user_username] = dict(zip(keys, values))
    return users_dict


def get_user_by_username(username):
    users = get_users()
    user = users.get(username)
    if user:
        return user


def add_user_to_file(username, password, fname, lname, city, email):
        handler = open('user.txt', 'a')
        password_in_bytes = bytes(password, 'utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password_in_bytes, salt)
        handler.write(f'{username}??{hashed_password.decode("utf-8")}??{fname}??{lname}??{city}??{email}@@@')
        handler.close()


def show_user_info(username):
    user = get_user_by_username(username)

    print('Username: ', username)
    for key, value in user.items():
        print(f'{key.capitalize()} : {value}')
    else:
        print('')


def show_users_list():
    users = get_users()

    t = PrettyTable(['Username', ])
    for user in users.keys():
        t.add_row([user])
    print(t)
    