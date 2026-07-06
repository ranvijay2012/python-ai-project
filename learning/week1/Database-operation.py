import mysql.connector
 
dataBase = mysql.connector.connect(
  host ="localhost",                # Localhost for local connection
  user ="root",
  passwd ="root",
  database ="rs_dev_db"
)

#prepare a cusror object using cursor() method
cursorObject = dataBase.cursor()

student_table_drop = input("Do you want to drop the student table? (yes/no): ")
if student_table_drop.lower() == "yes":
    cursorObject.execute("DROP TABLE IF EXISTS student")
    print("Table 'student' has been dropped.")


#if student table already existd then dont create it again
cursorObject.execute("SHOW TABLES LIKE 'student'")
table_exists = cursorObject.fetchone()

if table_exists:
  print("Table 'student' already exists.")
else:
  print("Table 'student' does not exist. Creating table...")

  #create student table in database
  studentRecord = """CREATE TABLE STUDENT (
                  NAME  VARCHAR(20) NOT NULL,
                  BRANCH VARCHAR(50),
                  ROLL INT NOT NULL,
                  SECTION VARCHAR(5),
                  AGE INT
  )"""

  #table created and table name is student
  cursorObject.execute(studentRecord)

#prpepare SQL query to INSERT a record into the database.
sql = "INSERT INTO STUDENT (NAME, BRANCH, ROLL, SECTION, AGE) VALUES (%s, %s, %s, %s, %s)"
val = [
    ("Alice", "Computer Science", 1, "A", 20),
    ("Bob", "Mechanical Engineering", 2, "B", 21),
    ("Charlie", "Electrical Engineering", 3, "C", 19)
]
cursorObject.executemany(sql, val)
print(cursorObject.rowcount, "records inserted successfully into student table.")

#execute the SQL query
cursorObject.executemany(sql, val)

# Commit the transaction so changes are saved
dataBase.commit()

#prepare quersy to select all records from the student table
sql = "SELECT * FROM STUDENT"
cursorObject.execute(sql)
records = cursorObject.fetchall()

for record in records:
    print(record)

#database connection closed
dataBase.close()


