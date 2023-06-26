# this script will insert data into a SQLite db

import sqlite3

# connect to the sqlite db file and create cursor
con = sqlite3.connect('database.db')
cur = con.cursor()

# data you will insert into the db, make sure it matches the schema and columns
new_rows = [
    ('10.0.0.1', 'hack.you.local', 1337),
    ('10.0.0.2', 'shells.payloads.exploits', 31337)
]

cur.executemany("INSERT INTO 'ips' VALUES(?,?,?)", new_rows)
con.commit()

cur.execute("SELECT * FROM 'ips'")
print(cur.fetchall())