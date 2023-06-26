# you need to run the following command to install the library
# pip3 install tabula-py
# This script will extract a table from a pdf and output into a csv but you need to specify the page

import tabula

table = tabula.read_pdf('weather.pdf', pages=1)

print(table[0])

table[0].to_csv('output.csv', index=None)