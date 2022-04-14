import sqlite3


#users table
try:
    sqliteConnection = sqlite3.connect('pythonsqlite.db')
    sqlite_create_table_users = '''CREATE TABLE IF NOT EXISTS users (
                                Id INTEGER PRIMARY KEY IDENTITY,
                                username Character NOT NULL UNIQUE,
                                firstname TEXT NOT NULL,
                                lastname TEXT NOT NULL,
                                password Character NOT NULL,
                                email Character NOT NULL,
                                city text NOT NULL);'''

    cursor = sqliteConnection.cursor()
    cursor.execute(sqlite_create_table_users)
    sqliteConnection.commit()
    print("Successfully users table created")

    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a users table", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        

#score table
try:
    sqliteConnection = sqlite3.connect('pythonsqlite.db')
    sqlite_create_table_score = '''CREATE TABLE IF NOT EXISTS score (
                                id INTEGER PRIMARY KEY,
                                username TEXT NOT NULL,
                                score TEXT NOT NULL);'''

    cursor = sqliteConnection.cursor()
    cursor.execute(sqlite_create_table_score)
    sqliteConnection.commit()
    print("Successfully score table created")

    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a score table", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        