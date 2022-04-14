import sqlite3
import termcolor2


def show_users_list():
    try:
        sqliteConnection = sqlite3.connect('pythonsqlite.db')
        cursor = sqliteConnection.cursor()
        
        user_list = "SELECT username FROM users;"
        count = cursor.execute(user_info)
        user_name = count.fetchall()
        print(user_name)
        cursor.close()
    except sqlite3.Error as error:
        print(termcolor2.colored("something wrong with show user list!!", color="red"), error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()



def show_user_info(username):
    try:
        sqliteConnection = sqlite3.connect('pythonsqlite.db')
        cursor = sqliteConnection.cursor()
        
        user_info ="""SELECT * FROM users WHERE username = '{username}';"""
        
        count = cursor.execute(user_info)
        info = count.fetchone()
        print(info)
        cursor.close()
        
    except sqlite3.Error as error:
        print(termcolor2.colored("something wrong with show user info!!", color="red"), error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
