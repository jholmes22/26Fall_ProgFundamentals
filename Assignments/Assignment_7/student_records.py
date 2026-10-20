import sqlit3 
conn = sqlite3.connect("StudentRecord.db") # opens school.db, or creates it
cur = conn.cursor() # the cursor runs SQL commands
# Remove the old table, so this step can be run again.
cur.execute("DROP TABLE IF EXISTS StudentRecords")
cur.execute("""
CREATE TABLE StudentRecord
( id INT,
name VARCHAR(30),
age INT,
major VARCHAR(30) )
""")
students = [
(1, "Nevaeh", 20, 'Computer science'),
(2, "Jaeden", 19, 'psychology'),
(3, "Gabby", 18, 'Kinesiology'),
(4, "Julyah, 23, 'Cosmetology'),
(5, "Aaliyah", 20, 'Nursing')
]
cur.exeutemany("INSERT INTO StudentRecords(id, name, age, major) VALUES(?, ?, ?, ?)", students)
for students in students:
  print(f"name{student[1]}, age{student[2]}, major{student[3]}")
while True:
  students = input("Do you want to add a new student? yes or no ").lower()
  if students == "yes": 
    while True:
      name = input("Enter a name ")
      if name != "":
        break
      print("name cannot be empty")
    while True:
      try:
        age = int(input("Enter a age "))
        break
      except ValueError:
        print("age must be a whole number")
    while True:
        major = input("Enter student major ")
      if major != "":
        break
      print("major cannot be empty")
    cur.execute("SELECT MAX(id) FROM StudentRecords")
    new_id = cursor.fetchone()[0]+1
    cur.execute("INSERT INTO StudentRecords(id, name, age, major) VALUES(?, ?, ?, ?)", (new_id, name, age, major) )
      break
  elif students == "no":
    print("No new students")
      break
  else:
    print("please enter yes or no")
  conn.commit()
  conn.close()
