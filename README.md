# Python Projects 
Projects from the Python course at The Tech Academy.
```
All projects written in Python 3.9.4
```

## [Nice or Mean Game](https://github.com/aglorenz/Python-Projects/tree/main/Nice%20or%20Mean%20Game)
A simple follow along exercise that creates a game using multiple parameterized functions.  If player select N (nice) they get 1 point for being nice.  If they select M they get 1 point for being mean.  Game loops until palyer reaches 3 nice or 3 mean points.  An appopriate message is printed depending if the player is nice or mean.

**Enhancement:**  I added audio capability by playing a different Homer Simpson sound depending on the win/lose result.

## [Database SQLite3](https://github.com/aglorenz/Python-Projects/tree/main/Database%20SQLite3)
From a list of files, select the names that have .txt extension and store them in a SQLite3 database.  Next, query them from the database and print them out to the console.  I created functions with parameters to make them more flexible.  They work with any file extension, table name, and open db connection passed to them.
```
createTable(conn, tblName)
storeFileList(conn, tblName, fileList, ext)
printFileList(conn, tblName)
```

## [Inheritance](https://github.com/aglorenz/Python-Projects/tree/main/Inheritance)
Demonstrate Classes, Inheritance, and a parameterized class constructor.

## [Polymorphism](https://github.com/aglorenz/Python-Projects/tree/main/Polymorphism)
* Create two classes (Automobile, Airplane) that inherit from a parent (Vehicle) class.
* Ensure the parent class has at least one method.
* Each child class declares the method with the same name as the parent and overrides the parent method with a different implementation.

**Enhancement:** I learned how to use multi-line f strings for the method output.
