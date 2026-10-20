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
  (2, 'The House on Mango Street', 'Sandra Cisneros', 1983, 'Novel', 40, 3),
  (3, 'The Great Gatsby', 'Scott Fitzgerald', 1925, 'Literary Fiction', 100, 4),
  (4, 'Frankenstien', 'Mary Shelley', 1818, 'Science Fiction', 30, 4),
  (5,
