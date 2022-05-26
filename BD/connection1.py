import mysql.connector
from mysql.connector import Error

class DAO1():

    def __init__(self):

        try:
            self.conexion=mysql.connector.connect(
              host='localhost',
              port=8889,
              user='root',
              passwd='root',
              db='Pasas1'
            )
        except Error as ex:
            print("Error al intentar la conexion: {0}".format(ex)) 

    def insertLog(self,cur):
        if self.conexion.is_connected():
            try:
                log=self.conexion.cursor()
                sql="INSERT INTO `WWW` (`Id`, `core`, `dd`) VALUES (NULL, {0}, {1});"
                log.execute(sql.format(cur[0],cur[1]))
                self.conexion.commit()
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex)) 

    def createTable (self):
        if self.conexion.is_connected():
            try:
                log=self.conexion.cursor()
                log.execute("CREATE TABLE WWW ( Id int PRIMARY key AUTO_INCREMENT, core varchar(20) not null,  dd varchar(30) not null  ); ")
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))  

    def dropTable (self):
        if self.conexion.is_connected():
            try:
                log=self.conexion.cursor()
                log.execute("DROP TABLE www")
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))    