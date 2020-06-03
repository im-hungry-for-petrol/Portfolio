import sqlite3

"""
Connecting to SQLite
"""
try:
    sqliteConnection = sqlite3.connect('Admin_Storage.db')
    sqlite_create_table_query = '''CREATE TABLE Admin_Sign_In (
                                id INTEGER PRIMARY KEY,
                                username TEXT NOT NULL,
                                password TEXT NOT NULL);'''

    cursor = sqliteConnection.cursor()


    cursor.execute(sqlite_create_table_query)
    sqliteConnection.commit()
    cursor.close()

except sqlite3.Error as error:
    print("error: ", error)
finally:
    if(sqliteConnection):
        sqliteConnection.close()
        print("Connection is closed!")
