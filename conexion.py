import mysql.connector
from mysql.connector import Error


class Cone( ):
    USER= None
    PASS= None
    HOST= None
    DB= None
    PORT= None

    conn= None

    def __init__(self,USER,PASS,HOST,DB,PORT):

        self.USER= USER
        self.PASS= PASS
        self.HOST= HOST
        self.DB= DB
        self.PORT= PORT

        try:
            self.conexion = mysql.connector.connect(
                host=self.HOST,
                port=self.PORT,
                user=self.USER,
                passwd=self.PASS,
                db= self.DB
            )
            
            if( self.conexion.is_connected()):
                print("conexion exitos")
        except mysql.connector.Error as ex: 
            print("Error durante la concexion: " ,ex)  

    def listt (self,sql):
            if self.conexion.is_connected():
                try:
                    log=self.conexion.cursor()
                    log.execute(sql)
                    resul= log.fetchall()
                    return resul
                except mysql.connector.Error  as ex:
                    print("Error truncateCourse_viewed: {0}".format(ex))


    def insert(self,sql,resul):
            if self.conexion.is_connected():
                try:
                    cursor=self.conexion.cursor()
                    cursor.executemany(sql,resul)
                    self.conexion.commit()
                except mysql.connector.Error as ex:
                    print("Error insertCourse_viewed: {0}".format(ex)) 

    def truncate (self,truncte):
            if self.conexion.is_connected():
                try:
                    log=self.conexion.cursor()
                    log.execute(truncte)
                except mysql.connector.Error as ex:
                    print("Error User_loggedin: {0}".format(ex))

       
                