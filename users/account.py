from .add_users import add_users_data_in_tupple
from .logger import log_user_register
from datetime import datetime
import sqlite3
import termcolor2
import bcrypt


def register(username, password, fname, lname, city, email):  
    add_users_data_in_tupple(username, password, fname, lname, city, email)
    log_user_register(username, datetime.now().replace(microsecond=0))


def login(username, password):
    try:
        sqliteConnection = sqlite3.connect('pythonsqlite.db')
        cursor = sqliteConnection.cursor()
        
        get_user = "SELECT * FROM user WHERE '{username}' AND Password = '{password}';"
        count = cursor.execute(get_user)
        user = count.fetchone()
        return user[id]
        
        if not cur.fetchone():
            print(termcolor2.colored(f'"{username}" does not exist!', color="red"))
            return None
            
        else:
            user_password = bytes(users.get(username).get('password'), 'utf-8')
            if bcrypt.checkpw(bytes(user['password'], 'utf-8'), user_password):
                print(termcolor2.colored(f'\n{username} Logged in successfully. ', color="green"))
                return True
            
            return user['id']
        cursor.close()
           
    except sqlite3.Error as error:
        print(termcolor2.colored("something wrong with get user!!", color="red"), error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
