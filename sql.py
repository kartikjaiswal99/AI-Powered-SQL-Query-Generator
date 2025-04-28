import sqlite3

# create a SQLite database file & connect to sqlite
connection = sqlite3.connect("database.db")

# create a cursor object
cursor = connection.cursor()

# drop the table if it exists
cursor.execute("DROP TABLE IF EXISTS STUDENT;")
cursor.execute("DROP TABLE IF EXISTS COURSE;")
cursor.execute("DROP TABLE IF EXISTS TEACHER;")

# Create STUDENT table
cursor.execute("""
CREATE TABLE STUDENT(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME VARCHAR(25),
    CLASS_ID INT,
    SECTION VARCHAR(25),
    MARKS INT
);
""")

# Create COURSE table
cursor.execute("""
CREATE TABLE COURSE(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    COURSE_NAME VARCHAR(50),
    INSTRUCTOR_ID INT
);
""")

# Create TEACHER table
cursor.execute("""
CREATE TABLE TEACHER(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME VARCHAR(25),
    DEPARTMENT VARCHAR(50)
);
""")

# Insert records into TEACHER
cursor.execute("INSERT INTO TEACHER (NAME, DEPARTMENT) VALUES ('Dr. Smith', 'Data Science');")
cursor.execute("INSERT INTO TEACHER (NAME, DEPARTMENT) VALUES ('Dr. Johnson', 'DevOps');")
cursor.execute("INSERT INTO TEACHER (NAME, DEPARTMENT) VALUES ('Dr. Lee', 'AI and ML');")

# Insert records into COURSE
cursor.execute("INSERT INTO COURSE (COURSE_NAME, INSTRUCTOR_ID) VALUES ('Data Science', 1);")
cursor.execute("INSERT INTO COURSE (COURSE_NAME, INSTRUCTOR_ID) VALUES ('DevOps', 2);")
cursor.execute("INSERT INTO COURSE (COURSE_NAME, INSTRUCTOR_ID) VALUES ('AI Fundamentals', 3);")
cursor.execute("INSERT INTO COURSE (COURSE_NAME, INSTRUCTOR_ID) VALUES ('Cloud Computing', 2);")

# Insert records into STUDENT
cursor.execute("INSERT INTO STUDENT (NAME, CLASS_ID, SECTION, MARKS) VALUES ('John', 1, 'A', 85);")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS_ID, SECTION, MARKS) VALUES ('Jane', 1, 'B', 90);")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS_ID, SECTION, MARKS) VALUES ('Doe', 1, 'A', 78);")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS_ID, SECTION, MARKS) VALUES ('Alice', 2, 'B', 88);")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS_ID, SECTION, MARKS) VALUES ('Bob', 2, 'A', 92);")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS_ID, SECTION, MARKS) VALUES ('Charlie', 3, 'C', 80);")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS_ID, SECTION, MARKS) VALUES ('Daisy', 4, 'B', 75);")

# Print inserted STUDENT records
print("\nInserted STUDENT records:")
data = cursor.execute("SELECT * FROM STUDENT;")
for row in data:
    print(row)

# Print inserted COURSE records
print("\nInserted COURSE records:")
data = cursor.execute("SELECT * FROM COURSE;")
for row in data:
    print(row)

# Print inserted TEACHER records
print("\nInserted TEACHER records:")
data = cursor.execute("SELECT * FROM TEACHER;")
for row in data:
    print(row)

# Close the connection
connection.commit()
connection.close()