import sys
import mysql.connector
from mysql.connector import Error

info = None
cursor = None
connection = None

def close():
    cursor.close()
    connection.close()

def execute(syntax):
    cursor.execute(syntax)

def insert(table,args,values):
    cursor.execute("""INSERT INTO %(table)s (%(args)s) VALUES (%(values)s)""", {
        'table':table,
        'args':args,
        'values':values
    })
    result = cursor.fetchone()
    if result is None:
        return False
    return result    

def select(field,table,field2Name,field2):
    cursor.execute("""SELECT %(field)s FROM %(table)s WHERE %(field2Name)s = %(field2)s""", {
        'field': field,
        'table': table,
        'field2Name': field2Name,
        'field2': field2
    })
    result = cursor.fetchone()
    if result is None:
        return False
    return result

def connect(host,username,password):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=username,
            password=password
        )

        if connection.is_connected():
            info = connection.get_server_info()
            print("Connected to MySQL ", info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
    except Error as e:
        print("Error While Connecting To MySQL DataBase: " + e)
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL Connection Is Closed")