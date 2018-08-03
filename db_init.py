import sqlite3

sqlite_file = 'globaldata.db'    # name of the sqlite database file
table_name = 'userdata'  # name of the table to be created
new_field = 'userid' # name of the column
field_type = 'INTEGER'
new_field = 'geolocation'
field_type = 'INTEGER'
new_field = 'fav'
field_type = 'TEXT'  # column data type

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# Creating a new SQLite table with 1 column
c.execute('CREATE TABLE userData(`userid` INTEGER, `geolocation` INTEGER, fav TEXT)')


# Committing changes and closing the connection to the database file
conn.commit()
conn.close()
