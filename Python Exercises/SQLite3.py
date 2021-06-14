import sqlite3

# get personal data from the user
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))

# execute insewrt statement for supplied person data
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    line = "INSERT INTO People VALUES ('"+ first_name +"', '"+ last_name +"', " +str(age) +")"
    print(line)

    # example: INSERT INTO People VALUES ('Mark', 'Lorenz', 44)
    # example with O'malley: INSERT INTO People VALUES ('James', 'O'malley', 22) fails because of quote in O'malley
    # c.execute(line)

    # this can be problematic if we try to insert somebody with name O'malley
    # To avoid this, we should have used placeholders in our SQL code and inserted the person data as a tuple.

person_data = (first_name, last_name, age)

print("INSERT INTO People VALUES {}".format(person_data))
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("INSERT INTO People VALUES(?, ?, ?)", person_data)
    c.execute("UPDATE People SET Age = ? WHERE FirstName = ? AND LastName=?",
              (45, 'James',"O'malley"))

# dropping the db and starting over
# demonstrating inserting multiple rows with executemany

people_values = (('Ron','Obvious',42), ('Luigi','Vercotti', 43), ('Arthur','Belling', 28))
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS People")
    c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
    c.executemany("INSERT INTO People VALUES(?, ?, ?)", people_values)

# select all first and last name from people over age 30
##    c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
##    for row in c.fetchall():
##        print(row)

##    c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
##    while True:
##        row = c.fetchone()
##        if row is None:  # None keyword is how to check objects for no value
##            break
##        print(row)
        
    c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
    row = c.fetchone()
    while row is not None:
        print(row)
        row = c.fetchone()
