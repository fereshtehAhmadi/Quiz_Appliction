import sqlite3

try:
    sqliteConnection = sqlite3.connect('pythonsqlite.db')
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")
    
    
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        
