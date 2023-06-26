# this script will extract data from a SQLite db

import sqlite3

# connect to the sqlite db file and create cursor
con = sqlite3.connect('database.db')
cur = con.cursor()

# Execute sql commands here - uncomment the queries below

# Show all tables
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cur.fetchall())

# run the command to print all the data from the table called ips
# cur.execute("SELECT * FROM 'ips' ")
# print(cur.fetchall())

# Grab data from a column
# cur.execute("SELECT address, asn FROM 'ips' ")
# print(cur.fetchall())

# Grab rows with asn less than 200
# cur.execute("SELECT address, asn FROM 'ips' WHERE asn < 200")
# print(cur.fetchall())

# Grab rows with asn of 198
# cur.execute("SELECT address, asn FROM 'ips' WHERE asn = 198")
# print(cur.fetchall())

# Filter for keywords
# cur.execute("SELECT address, asn FROM 'ips' WHERE asn < 300 AND domain LIKE '%sa'")
# print(cur.fetchall())