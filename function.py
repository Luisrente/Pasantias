
from connection import Connect
from mysql.connector import Error


def listCourse_viewed(con):
    if ( con.conexion.is_connected()):
        try:           
            log=con.conexion.cursor()
            log.execute("SELECT `component`,`userid`FROM `mdl_logstore_standard_log` WHERE `crud`='c';")
            resultados= log.fetchall()
            return resultados
        except Error as ex:
            print("Error listCourse_viewed: {0}".format(ex)) 


def truncateCourse_viewed (con):
        if con.conexion.is_connected():
            try:
                log=con.conexion.cursor()
                log.execute("TRUNCATE TABLE WWW")
            except Error as ex:
                print("Error truncateCourse_viewed: {0}".format(ex))


def insertCourse_viewed(con,resul):
    truncateCourse_viewed(con)
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