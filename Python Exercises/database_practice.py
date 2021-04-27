
import sqlite3

conn = sqlite3.connect('test.db')  # create db if it doesn't exist

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT, \
        col_lname TEXT, \
        col_email TEXT \
        )")
    conn.commit()
conn.close()  # not needed since we are using 'with conn:'

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) \
            VALUES (?,?,?)", ('Sarah', 'Jones', 'sjones@gmail.com'))
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) \
            VALUES (?,?,?)", ('Sally', 'May', 'sallymay@gmail.com'))
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) \
        VALUES (?,?,?)", ('Kevin', 'Bacon', 'kbacon@rocketmail.com'))

    conn.commit()
conn.close()   # not needed since we are using 'with conn:'

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fname, col_lname, col_email FROM tbl_persons WHERE col_fname = 'Sarah'")
    varPerson = cur.fetchall()
    for item in varPerson:
        msg = "FirstName: {}\nLast Name: {}\nEmail: {}".format(item[0], item[1], item[2])
    print(msg)
