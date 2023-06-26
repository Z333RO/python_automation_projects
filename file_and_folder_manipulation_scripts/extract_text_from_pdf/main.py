#this script will grab text from pdf and print on screen - can be useful for grepping on pdf files
#replace "place_holder.pdf" with the pdf file you want to extract data from in the current directory.

import fitz

with fitz.open("place_holder.pdf") as pdf:
    for page in pdf:
        # uncomment below to have a divider between pages 
        # print(20 * '-')
        print(page.get_text())

# If you need to grab text only from one page, just uncomment the below code. It will grab from the first page. Just replace the data in the index[x]
# with fitz.open("place_holder.pdf") as pdf:
#     page1 = pdf[0].get_text()
#     print(page1)

# uncomment to grab strings from ALL pages
# with fitz.open("place_holder.pdf") as pdf:
#     text = ''
#     for page in pdf:
#         text = text + page.get_text()
#         print(text)