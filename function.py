
import string
from typing import Sized
from unicodedata import name
import csv
from datetime import datetime

class Function():

    conexion= None


    def __init__(self, conexion,conexion1):
        self.conexion= conexion
        self.conexion1= conexion1

    def createFile(self,name,resul):
        date=(datetime.today().strftime('%Y-%m-%d'))
        file= "csv/"+name+date+".csv"
        archivo = open(file,"w")
        write= csv.writer(archivo, delimiter=',')
        write.writerows(resul)

    def insertCourse_viewed(self):
        sql="SELECT id,eventname,component,action,crud,userid,courseid,from_unixtime(timecreated) AS Date FROM mdl_logstore_standard_log WHERE eventname='\\\\core\\\\event\\\\course_viewed';"
        sql1="TRUNCATE TABLE Course_viewed"
        sql2="""INSERT INTO `Course_viewed` (`id`, `idevent`, `eventname`, `component`, `action`, `crud`, `userid`, `courseid`, `Date`) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s)"""
        try:
            resul= self.conexion.select(sql)
            print("Course_viewed")
            print(len(resul))
            self.conexion1.truncate(sql1)
            self.conexion1.insert(sql2,resul)
            Function.createFile(self,'Course_viewed',resul)
        except:
            print("Error insertCourse_viewed")


    def insertUser_loggedin(self):
        sql="SELECT `id`,`eventname`,`component`,`action`,`crud`,`userid`,`courseid`,from_unixtime(timecreated) AS 'Date' FROM `mdl_logstore_standard_log` WHERE `eventname`='\\\\core\\\\event\\\\user_loggedin';"
        sql1="TRUNCATE TABLE User_loggedin"
        sql2="""INSERT INTO `User_loggedin` (`id`, `idevent`, `eventname`, `component`, `action`, `crud`, `userid`, `courseid`, `Date`) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s)"""
        
        try:
            resul= self.conexion.select(sql)
            print("User_loggedin")
            print(len(resul))
            self.conexion1.truncate(sql1)
            self.conexion1.insert(sql2,resul)
            name='User_loggedin'
            Function.createFile(self,name,resul)
        except:
            print("Error insertUser_loggedin")













