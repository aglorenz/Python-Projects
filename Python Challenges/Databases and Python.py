import sqlite3
from tabulate import tabulate

# open database in RAM
##with sqlite3.connect(':memory:') as connection:
##    c = connection.cursor()

conn = sqlite3.connect(':memory:') # db in RAM
with conn: 
    cur = conn.cursor()

    # Create the table
    sqlcmd = "CREATE TABLE if not exists Roster( \
        name TEXT, species TEXT, IQ INT)" 
    print("\n"+sqlcmd)
    cur.execute(sqlcmd)

    # populate with 5th element movie characters
    people_values = (('Jean-Baptiste Zorg','Human',122),
                     ('Korben Dallas','Meat Popsicle',100),
                     ("Ak'not",'Mangalore',-5))
    cur.executemany("INSERT INTO Roster VALUES(?, ?, ?)", people_values)

    # update a row
    sqlcmd = """
        UPDATE Roster 
        SET species = 'Human'
        WHERE name like 'Kor%'
        """
    print(sqlcmd)
    cur.execute(sqlcmd)

    # print two columns from each row one at a time
    print("\nTable output using fetchone() and while row is not None:")
    sqlcmd = """
        SELECT name, IQ 
        FROM Roster 
        WHERE species = 'Human'
        """
    print(sqlcmd)
    cur.execute(sqlcmd)
    for row in cur.fetchall():
        print(row)
    
##    row = cur.fetchone()
##    while row is not None:
##        print("Name: {}, IQ: {}".format(row[0], row[1]))
##        row = cur.fetchone()
##
##    # print the rows all at once using tabulate
##    print("\n\nTable output using fetchall() and tabulate module")
##    print(sqlcmd)
##    cur.execute(sqlcmd)
##    data = cur.fetchall()
##    print (tabulate(data, headers=["Name","IQ"])) 
