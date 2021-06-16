import sqlite3

# open database in RAM
##with sqlite3.connect(':memory:') as connection:
##    c = connection.cursor()

conn = sqlite3.connect(':memory:') # db in RAM
with conn: 
    cur = conn.cursor()

    # Create the table
    sqlcmd = "CREATE TABLE if not exists Roster( \
        name TEXT, species TEXT, IQ INT)" 
    print(sqlcmd)
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

    # print the rows
    sqlcmd = "SELECT * FROM Roster WHERE species = 'Human'"
    print(sqlcmd)
    cur.execute(sqlcmd)
    row = cur.fetchone()
    while row is not None:
        print(row)
        row = cur.fetchone()
              
