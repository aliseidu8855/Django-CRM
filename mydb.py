import pymysql

dataBase = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '199031552aA@'
)

#prepare a cursor object
cursorObject = dataBase.cursor()

#create a datebase
cursorObject.execute("CREATE DATABASE mydatabase")
print("All Done!")
