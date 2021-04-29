# Python Projects 
Projects from the Python course at The Tech Academy.
```
All projects written in Python 3.9.4
```

## [Nice or Mean Game](https://github.com/aglorenz/Python-Projects/tree/main/Nice%20or%20Mean%20Game)
A simple follow along game that uses multiple functions with parameters.  If player select N (nice) they get 1 point for being nice.  If they select M they get 1 point for being mean.  Game loops until palyer reaches 3 nice or 3 mean points.  An appopriate message is printed depending if the player is nice or mean.

**Enhancement:**  I added different Homer Simpson audio clips to be played depending on the nice or mean final score.

## [Database SQLite3](https://github.com/aglorenz/Python-Projects/tree/main/Database%20SQLite3)
From a list of files, select the names that have .txt extension and store them in a SQLite3 database.  Next query them from the database and print them out to the console.  I created functions with arguments to make them more flexible.  They work with any file extension, table name, and open db connection passed to them.
```
createTable(conn, tblName)
storeFileList(conn, tblName, fileList, ext)
printFileList(conn, tblName)
```

## [Inheritance](https://github.com/aglorenz/Python-Projects/tree/main/Inheritance)
Demonstrate Classes, Inheritance, and a parameterized class constructor
