import mysql.connector
from mysql.connector import Error

class DAO():

    def __init__(self):
        try:
            self.conexion=mysql.connector.connect(
              host='localhost',
              port=8889,
              user='root',
              passwd='root',
              db='Pasantia'
            )
        except Error as ex:
            print("Error al intentar la conexion: {0}".format(ex)) 

    def listLogs(self):
        if ( self.conexion.is_connected()):
            try:           
                log=self.conexion.cursor()
                log.execute("SELECT `component`,`userid`FROM `mdl_logstore_standard_log` WHERE `crud`='c';")
                resultados= log.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexion lis: {0}".format(ex))    