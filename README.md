# Python Projects 
**Projects from the Tech Academy Python course**
```
All projects written in Python 3.9.5 unless otherwise noted
```

## [Nice or Mean Game (3.9.4)](https://github.com/aglorenz/Python-Projects/tree/main/Nice%20or%20Mean%20Game)
A simple follow along exercise that creates a game using multiple parameterized functions.  If player select N (nice) they get 1 point for being nice.  If they select M they get 1 point for being mean.  Game loops until palyer reaches 3 nice or 3 mean points.  An appopriate message is printed depending if the player is nice or mean.

**Enhancement:**  I added audio capability by playing a different Homer Simpson sound depending on the win/lose result.

## [Database SQLite3 (3.9.4)](https://github.com/aglorenz/Python-Projects/tree/main/Database%20SQLite3)
From a list of files, select the names that have .txt extension and store them in a SQLite3 database.  Next, query them from the database and print them out to the console.  I created functions with parameters to make them more flexible.  They work with any file extension, table name, and open db connection passed to them.
```
createTable(conn, tblName)
storeFileList(conn, tblName, fileList, ext)
printFileList(conn, tblName)
```
## [Inheritance (3.9.4)](https://github.com/aglorenz/Python-Projects/tree/main/Inheritance)
Demonstrate Classes, Inheritance, and a parameterized class constructor.

## [Polymorphism (3.9.4)](https://github.com/aglorenz/Python-Projects/tree/main/Polymorphism)
* Create two classes (Automobile, Airplane) that inherit from a parent (Vehicle) class.
* Ensure the parent class has at least one method.
* Each child class declares the method with the same name as the parent and overrides the parent method with a different implementation.

**Enhancement:** I learned how to use multi-line f strings for the method output.

## [Student Tracking with Tkinter, Treeview, and SQLite3](https://github.com/aglorenz/Python-Projects/tree/main/StudentTrackingApp)
This application uses Tkinter and SQLite3 to gather Student data from 5 input fields, add the data to a database table, and display it on a Treeview widget. The application has the following buttons Add, Delete, and Close.  The delete function deletes all records selected from the Treeview and database.

**Notes**
* The primary key of the database is in Treeview column 0 and is hidden since it's not important to the user.
* Though this column is hidden, it's values are available for identifying db rows for deletion.

**What I learned**
* Currently learning proper use of docstrings and their different types...
* Treeview is great for tabular data and can be used for heirarchical tabular data.
* You can hide columns from the user and still have the data available to the program.
* The function, lastrowid, is handy for capturing the last id used when inserting a database row.
* I may need to research lastrowid to see if the id is always from the row you entered (when considering concurrency).  I used cursor.execute("BEGIN") to try to create a transaction.  I will test this someday as this concern is not critical on a single user database.

## [Encapsulation](https://github.com/aglorenz/Python-Projects/tree/main/Encapsulation)
**Demonstrate Encapsulation**
* Create a class that uses encapsulation.  The class should use:
  * A private attribute or function
  * A protected attribute or function
* Create an object that uses the protected and private attribute or function

## [Abstraction](https://github.com/aglorenz/Python-Projects/tree/main/Abstraction)
**Demonstrate Abstraction Concepts**
* Create a class with at least one abstract method and one regular method.
* Create a child class that implements the parent class's abstract method.
* Create at least one object that that utilizes both the parent and child methods

**What I learned**
* Abstract methods are useful for when we want to provide a common interface for different implementations of a component such as payment method.  Good for API's

## [Web Page Generator](https://github.com/aglorenz/Python-Projects/tree/main/Web Page Generator)
**Generate a Web Page With Python**
* Create an app that can generate a simple (hardcoded) web page at the click of a button
* Include a second button and an text Entry box to allow the user to create a customized verson of the web Page.

**What I learned**
* Assigning a '''comment''' to a variable can be an effective way to preseve the visual format of an HTML file.
