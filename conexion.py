import mysql.connector
from mysql.connector import Error


try:
    conexion = mysql.connector.connect(
        host='localhost',
        port=8889,
        user='root',
        passwd='root',
        db='Pasantia'
    )
    if( conexion.is_connected()):
        print("conexion exitos")
        #infoServer= conexion.get_server_info()
        #print("Informacion : ", infoServer)
        cursor= conexion.cursor()
        # cursor.execute("SELECT database();")
        #registro= cursor.fetchone()
        #print("Conectado a la DB: ", registro)
        cursor.execute("SELECT * FROM mdl_logstore_standard_log")
        resultados= cursor.fetchall()
        for fila in resultados:
            print("id:",[0])
except Error as ex: 
    print("Error durante la concexion: " ,ex)   

finally: 
    if conexion.is_connected():
        conexion.close() #Se cerro la conexion
        print("La conexion ha finalizado .")
        