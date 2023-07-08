content = """First Amendment 

Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof; or abridging the freedom of speech, or of the press; or the right of the people peaceably to assemble, and to petition the Government for a redress of grievances."""


with open('file.txt', 'w') as file:
    file.write(content)






# Below was the initial code - above is a variant, does the same thing.
# file = open('file1.txt', 'w')
# content = """First Amendment 

# Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof; or abridging the freedom of speech, or of the press; or the right of the people peaceably to assemble, and to petition the Government for a redress of grievances."""

# file.write(content)
# file.close()