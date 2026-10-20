import sqlit3 
conn = sqlite3.connect("library.db") # opens school.db, or creates it
cur = conn.cursor() # the cursor runs SQL commands
# Remove the old table, so this step can be run again.
cur.execute("DROP TABLE IF EXISTS books")
cur.execute("""
CREATE TABLE books
( id INT,
  title VARCHAR(30),
  author VARCHAR(30),
  year INT,
  genre VARCHAR(20),
  copies INT,
  rating INT
  PRIMARY KEY (id))
  """)
conn.commit() # save the changes to the file
conn.close()
print("The books table is ready.")
cur.execute("INSERT INTO books VALUES (1, 'The Very Hungry Caterpillar', 'Eric Carle', 1969, 'Kids' Book', 20, 5
)")
books = [
  (2, 'The House on Mango Street', 'Sandra Cisneros', 1983, 'Novel', 40),
  (3, 'The Great Gatsby', 'Scott Fitzgerald', 1925, 'Fiction', 100, 4),
  (4, 'Frankenstien', 'Mary Shelley', 1818, 'Science', 30, 4),
  (5, 'A Good Girls Guide To Murder', 'Holly Jackson', 2019, 'Mystery', 50, 4),
  (6, 'If He Had Been With Me', 'Laura Nowlin', 2013, 'Romance', 80, 2),
  (7, 'Harry Potter', 'J.K. Rowling', 1997, 'Fantasy', 500)
  (8, 'Pretend Shes Here, 'Luanne Rice', 2019, 'Fiction', 300, 5)
]
cur.executemany("INSERT INTO books VALUES (?, ?, ?, ?, ?, ?)", books)
conn.commit()
conn.close()
print("8 books added.")
print("title and author published after 1990")
for row in cur.execute("SELECT title, author FROM books WHERE >= 1990"):
  print(row)
print("title of fiction book with 2 or more copies")
for row in cur.execute("SELECT title FROM books WHERE genre = "fiction" AND copies >= 2"):
  print(row)
print("title published after 1990 or rated 5")
for row in cur.execute("SELECT title FROM books WHERE <1900 OR rating = 5"):
  print(row)
print("title that are not mystery")
for row in cur.execute("SELECT title FROM books WHERE NOT genre = "mystery""):
  print(row)
print("title that are history or science")
for row in cur.execute("SELECT TITLE FROM books WHERE genre IN ("science", "history")"):
  print(row)
letter = input("Enter Letter: ")
for row in cur.execute("SELECT author FROM books WHERE author LIKE ?",
(letter+"%",)
):
  print("Author: ", row[0])
print("title that have no rating")
for row in cur.execute("SELECT title FROM books WHERE rating IS NULL"):
  print(row)

