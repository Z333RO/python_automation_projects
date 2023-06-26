# this script will extract data from a SQLite db and convert it into a csv file

import sqlite3
import pandas

# connect to the sqlite db file and create cursor
con = sqlite3.connect('database.db')
cur = con.cursor()
# passing df as a variable for the data frame - pandas library
df = pandas.read_sql_query("SELECT * FROM 'ips' ORDER BY asn", con)
print(df)

df.to_csv('database.csv', index=None) # delete the index=None argument if you want to include the index numbers in the csv - not recommended
# uncomment to convert to xlsx file instead but need to install dependency 'pip install openpyxl'
# df.to_excel('database.xlsx', index=None)