import mysql.connector
import os

# clean the terminal screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
clear_screen()

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="canuKs01",
    database='teste'
)
cursor = mydb.cursor()
try:
    cursor.execute('CREATE DATABASE teste')

except mysql.connector.errors.DatabaseError:
    print('Database already exists')

try:
    cursor.execute('CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))')
except mysql.connector.errors.ProgrammingError:
    print('Table already exists')





