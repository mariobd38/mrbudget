import mysql.connector
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

def getUser():
    configure()
    return str(os.getenv('user'))

def getPasswd():
    configure()
    return str(os.getenv('passwd'))

mydb = mysql.connector.connect(
    host="localhost",
    user=getUser(),
    passwd=getPasswd(),
)
my_cursor = mydb.cursor()
# v = f'mysql+pymysql://{getUser()}:={getPasswd()},@localhost/our_users'
# print(v)
# my_cursor.execute("CREATE DATABASE testing")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)