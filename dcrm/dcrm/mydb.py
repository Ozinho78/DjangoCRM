# Install Mysql on your computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

# import mysql.connector
import pymysql

dataBase = pymysql.connect(
  host = 'localhost',
  user = 'root',
  passwd = 'Drucker1%'
  # database = 'mysql'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")