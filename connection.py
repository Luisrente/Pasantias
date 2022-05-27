import mysql.connector
from mysql.connector import errorcode

class Connect( ):
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

            conexion=conexion.mysql.connector.connect(
                                                   host=self.HOST,
                                                   port=self.PORT,
                                                   user=self.USER,
                                                   passwd=self.PASS,
                                                   db=self.DB)
            conexion.autocommit= False  
            self.conn=conexion
        except mysql.connector.ERROR as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password") 
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist ")
            else:
                print(err)    

    def listCourse_viewed(self, Query_params, params):
        if ( conn.conexion.is_connected()):
            try:           
                log=conn.conexion.cursor()
                log.execute("SELECT `component`,`userid`FROM `mdl_logstore_standard_log` WHERE `crud`='c';")
                resultados= log.fetchall()
                return resultados
            except mysql.connector.ERROR  as ex:
                print("Error listCourse_viewed: {0}".format(ex)) 

exec

    def truncateCourse_viewed ():
            if con.conexion.is_connected():
                try:
                    log=con.conexion.cursor()
                    log.execute("TRUNCATE TABLE WWW")
                except Error as ex:
                    print("Error truncateCourse_viewed: {0}".format(ex))


    def insertCourse_viewed(con,resul):
        truncateCourse_viewed()
        for insert in resul:
            if con.conexion.is_connected():
                try:
                    log=con.conexion.cursor()
                    sql="INSERT INTO `WWW` (`Id`, `core`, `dd`) VALUES (NULL, {0}, {1});"
                    log.execute(sql.format(insert[0],insert[1]))
                    con.conexion.commit()
                except Error as ex:
                    print("Error insertCourse_viewed: {0}".format(ex)) 


    def listuser_loggedin(con):
        if ( con.conexion.is_connected()):
            try:           
                log=con.conexion.cursor()
                log.execute("SELECT `component`,`userid`FROM `mdl_logstore_standard_log` WHERE `crud`='c';")
                resultados= log.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexion lis: {0}".format(ex)) 

    def truncateUser_loggedin (con):
            if con.conexion.is_connected():
                try:
                    log=con.conexion.cursor()
                    log.execute("TRUNCATE TABLE WWW")
                except Error as ex:
                    print("Error User_loggedin: {0}".format(ex))

    def insertUser_loggedin(con,resul):
        conte=Connect()
        if conte.conexion.is_connected():
            try:
                log=conte.conexion.cursor()
                sql="INSERT INTO `WWW` (`Id`, `core`, `dd`) VALUES (NULL, {0}, {1});"
                log.execute(sql.format(resul[0],resul[1]))
                conte.conexion.commit()
            except Error as ex:
                print("Error User_loggedin: {0}".format(ex))    