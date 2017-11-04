import csv
import sqlite3 as sq
test1 = 'This is a test of the emergency text system'
with open('test_Part_7.txt', 'wt') as outfile:
    outfile.write(test1)
with open('test_Part_7.txt', 'rt') as infile:
    test2 = infile.read()
print(test2 == test1)

text = '''title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Mieville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992
'''
with open('books.csv', 'wt') as cvsfileW:
    cvsfileW.write(text)

with open('books.csv', 'rt') as cvsfileR:
    books = csv.DictReader(cvsfileR)
    for book in books:
        print(book)
print(books)

db = sq.connect('books.db')
curs = db.cursor()
#curs.execute('''CREATE TABLE book (title text, author text, year int)''')
db.commit()

ins_str = 'INSERT INTO book values(?, ?, ?)'
with open('books.csv', 'rt') as infile:
    books = csv.DictReader(infile)
    for book in books:
        curs.execute(ins_str, (book['title'], book['author'], book['year']))

sql = 'SELECT author FROM book ORDER BY author ASC'
for row in db.execute(sql):
    print(row)