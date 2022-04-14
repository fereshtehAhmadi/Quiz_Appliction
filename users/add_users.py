import sqlite3
import termcolor2
import bcrypt
import hashlib


def add_users_data_in_tupple(username, password, fname, lname, city, email):
    password_in_bytes = bytes(password, 'utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_in_bytes, salt)
    new_user = (username, hashed_password.decode("utf-8"), fname, lname, city, email)
    add_user_to_db(new_user)
    

def add_user_to_db(new_user):
    try:
        sqliteConnection = sqlite3.connect('pythonsqlite.db')
        cursor = sqliteConnection.cursor()
        
        sqlite_insert_query ="""INSERT INTO users 
                            (username, firstname, lastname, password, email, city) 
                            VALUES(?, ?, ?, ?, ?, ?);""", new_user
                                
        
        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        print(termcolor2.colored("Your information was successfully registered.", color= "green"), cursor.rowcount)
        
        cursor.close()

    except sqlite3.Error as error:
        print(termcolor2.colored("Not registered!!", color="red"), error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
                