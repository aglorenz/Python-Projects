
def createTable(conn, tblName):
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS {}( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            filename TEXT)".format(tblName))
        conn.commit()

def storeFileList(conn, tblName, fileList, ext):
    #print(type(fileList)) # fileList is a tuple
    with conn:
        cur = conn.cursor()
        for name in fileList:
            if ext in name:
                # remember to use a comma to indicate the list is a tuple or use [name]
                cur.execute("INSERT INTO {}(filename) VALUES(?)".format(tblName), (name,))
            conn.commit()

def printFileList(conn, tblName):
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM {} ".format(tblName))
        retRows = cur.fetchall()
        for name in retRows:
            #print(type(name)) # each row returned is a tuple
            print("File name: {}".format(name[1]))
            
##    varPerson = cur.fetchall()
##    for item in varPerson:
##        msg = "FirstName: {}\nLast Name: {}\nEmail: {}".format(item[0], item[1], item[2])
##    print(msg)
        
        
#conn.close()  # not needed since we are using 'with conn:'
##
##conn = sqlite3.connect('test.db')
##
##with conn:
##    cur = conn.cursor()
##    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) \
##            VALUES (?,?,?)", ('Sarah', 'Jones', 'sjones@gmail.com'))
##    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) \
##            VALUES (?,?,?)", ('Sally', 'May', 'sallymay@gmail.com'))
##    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) \
##        VALUES (?,?,?)", ('Kevin', 'Bacon', 'kbacon@rocketmail.com'))
##
##    conn.commit()
##conn.close()   # not needed since we are using 'with conn:'
##
##conn = sqlite3.connect('test.db')
##
##with conn:
##    cur = conn.cursor()
##    cur.execute("SELECT col_fname, col_lname, col_email FROM tbl_persons WHERE col_fname = 'Sarah'")
##    varPerson = cur.fetchall()
##    for item in varPerson:
##        msg = "FirstName: {}\nLast Name: {}\nEmail: {}".format(item[0], item[1], item[2])
##    print(msg)

def main():
    import sqlite3
    dbName = 'myDatabase.db'
    tblName = 'txt_filenames'
    ext = 'txt'

    # From a list of files, grab the file names with the .txt extension and store them in a database
    fileList = ('information.docx','Hello.txt','myImage.png', \
                'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

    conn = sqlite3.connect(dbName)    # Create the db if it doesn't exist
    createTable(conn, tblName)        # Create table if it doesn't exist

    storeFileList(conn, tblName, fileList, ext) # store qualifying file name in the db
    printFileList(conn, tblName)                # Print list of text filenames to the console
        
    
if __name__ == "__main__":
    main()
    
