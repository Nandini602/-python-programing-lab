'''
a) Create a database in MySQL with a table of students. The table will contain the following 
fields: 
1. PRN number #this will be a primary key
2. First Name
3. Middle name
4. Last name
5. Address
6. mobile number
7. email id
8. DOB
b) Insert 4-5 records in the table.

'''

import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="MYSQL")
mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE students_data")


mydb = mysql.connector.connect(host="localhost",user="root",passwd="tanvi",database="students_data")
mycursor = mydb.cursor()
mycursor2 = mydb.cursor()
#mycursor.execute("CREATE TABLE students_data (PRN VARCHAR (255) PRIMARY KEY, First_name VARCHAR(255), Middle_name VARCHAR(255), Last_name VARCHAR(255), Address VARCHAR(255), Mobile_Number VARCHAR(200) , Email_id VARCHAR(255), Date_of_Birth VARCHAR(255))")

print("Structure of Table students_data : ")
mycursor2.execute("DESCRIBE students_data.students_data")
table = mycursor2.fetchall()
print(table)


sql = "INSERT INTO students_data (PRN, First_name,Middle_name, Last_name,Address,Mobile_Number,Email_id,  Date_of_Birth ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

student1 = ("2130331245501","nandini","narendra","mendhe","nagpur","9112974690","mendhenandini@gmail.com","2002-06-02")
student2 = ("2130331245502"," nandesh ","narendra ","mendhe","nagpur","1233456784","nandeshmendhe92@gmail.com","2001-05-2")
student3 = ("2130331245503","vedika ","sunil","peshane","Amravati","9067358295","peshaneved@gmail.com","2002-02-14")
student4 = ("2130331245504"," Gayatri","sanjay","mugale","chandrapur","8237677828","@gmail.com","2003-07-23")
student5 = ("2130331245505"," sunanda "," narendra","kale"," chimur","9420644874","sunanda123@gmail.com","2002-06-26")

mycursor.execute(sql,student1)
mycursor.execute(sql,student2)
mycursor.execute(sql,student3)
mycursor.execute(sql,student4)
mycursor.execute(sql,student5)
mydb.commit()

print ("Records Inserted!")
print()
print(" students_data Table contains following data :")
query ="SELECT * FROM students_data"
mycursor.execute(query)
for x in mycursor:
    print(x) 
t