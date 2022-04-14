import sqlite3


try:
    sqliteConnection = sqlite3.connect('pythonsqlite.db')
    sqlite_create_table_logg = '''CREATE TABLE IF NOT EXISTS logger (
                                username Character NOT NULL UNIQUE,
                                logg Character NOT NULL UNIQUE
                                );'''

    cursor = sqliteConnection.cursor()
    cursor.execute(sqlite_create_table_logg)
    sqliteConnection.commit()
    print("Successfully logger table created")

    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a logger table", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        







def log_user_register(username, date_time_obj):
    try:
        sqliteConnection = sqlite3.connect('pythonsqlite.db')
        cursor = sqliteConnection.cursor()
        
        sqlite_insert_query ="""INSERT INTO logger 
                            (username, logg) 
                            VALUES({'username}','{date_time_obj}');"""
                                
        
        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        
        cursor.close()

    except sqlite3.Error as error:
        print(termcolor2.colored("Not registered user logg!!", color="red"), error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
