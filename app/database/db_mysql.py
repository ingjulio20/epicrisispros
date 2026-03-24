import mysql.connector

def mysql_connection():
    user = 'root'
    password = ''
    host = 'localhost'
    database = 'pros_hc'
    port = 3306
    conexion = mysql.connector.connect(
        user = user,
        password = password,
        host = host,
        database = database,
        port = port
    )

    return conexion