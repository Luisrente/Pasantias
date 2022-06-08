
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

    def insertUser_loggedin(self):
        sql="SELECT mdl_pregrado_2021_2.mdl_logstore_standard_log.id, mdl_pregrado_2021_2.mdl_logstore_standard_log.eventname, mdl_pregrado_2021_2.mdl_logstore_standard_log.component, mdl_pregrado_2021_2.mdl_logstore_standard_log.action, mdl_pregrado_2021_2.mdl_logstore_standard_log.objecttable, mdl_pregrado_2021_2.mdl_logstore_standard_log.objectid, mdl_pregrado_2021_2.mdl_logstore_standard_log.crud, mdl_pregrado_2021_2.mdl_logstore_standard_log.edulevel, mdl_pregrado_2021_2.mdl_logstore_standard_log.ip, mdl_pregrado_2021_2.mdl_logstore_standard_log.other, DATE_FORMAT(FROM_UNIXTIME(mdl_pregrado_2021_2.mdl_logstore_standard_log.timecreated),'%Y-%m-%d %H:%i') AS timecreated, mdl_pregrado_2021_2.mdl_logstore_standard_log.origin, mdl_pregrado_2021_2.mdl_logstore_standard_log.userid, mdl_pregrado_2021_2.mdl_user.username, mdl_pregrado_2021_2.mdl_user.idnumber, mdl_pregrado_2021_2.mdl_user.firstname, mdl_pregrado_2021_2.mdl_user.lastname, mdl_pregrado_2021_2.mdl_user.email, mdl_pregrado_2021_2.mdl_course.id, mdl_pregrado_2021_2.mdl_course.fullname , mdl_pregrado_2021_2.mdl_course.shortname , mdl_pregrado_2021_2.mdl_course.idnumber, mdl_pregrado_2021_2.mdl_course.startdate , mdl_pregrado_2021_2.mdl_course.enddate , mdl_pregrado_2021_2.mdl_course.category, mdl_pregrado_2021_2.mdl_course_categories.name, mdl_pregrado_2021_2.mdl_course_categories.idnumber, mdl_pregrado_2021_2.mdl_course_categories.parent, mdl_pregrado_2021_2.mdl_course_categories.coursecount, mdl_pregrado_2021_2.mdl_course_categories.depth, mdl_pregrado_2021_2.mdl_course_categories.path FROM mdl_pregrado_2021_2.mdl_logstore_standard_log LEFT JOIN mdl_pregrado_2021_2.mdl_user ON  mdl_pregrado_2021_2.mdl_logstore_standard_log.userid= mdl_pregrado_2021_2.mdl_user.id LEFT JOIN mdl_pregrado_enroll.matricula ON mdl_pregrado_2021_2.mdl_user.idnumber=mdl_pregrado_enroll.matricula.idusuario LEFT JOIN mdl_pregrado_2021_2.mdl_course ON  mdl_pregrado_2021_2.mdl_course.idnumber= mdl_pregrado_enroll.matricula.idcurso LEFT JOIN mdl_pregrado_2021_2.mdl_course_categories ON  mdl_pregrado_2021_2.mdl_course.category=      mdl_pregrado_2021_2.mdl_course_categories.id WHERE mdl_pregrado_2021_2.mdl_logstore_standard_log.eventname='\\\\core\\\\event\\\\user_loggedin' LIMIT 10"
        sql1="TRUNCATE TABLE user_loggedin"
        sql2="""INSERT INTO `user_loggedin` (`id_event`, `eventname`,`component`, `action`, `objecttable`, `objectid`, `crud`, `edulevel`, `courseid`, `other`,`timecreated`, `origin`, `userid`, `username`,`ip` `idnumber`, `firstname`, `lastname`, `email`) VALUES (%s,%s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s,%s,%s)"""
        try:
            resul= self.conexion.select(sql)
            print("User_loggedin")
            print(len(resul))
            self.conexion1.truncate(sql1)
            self.conexion1.insert(sql2,resul)
            Function.createFile(self,'User_loggedin',resul)
        except:
            print("Error insertCourse_viewed")


    def insertCourse_viewed(self):
        sql="SELECT mdl_logstore_standard_log.id, mdl_logstore_standard_log.eventname, mdl_logstore_standard_log.component, mdl_logstore_standard_log.action, mdl_logstore_standard_log.objecttable, mdl_logstore_standard_log.objectid, mdl_logstore_standard_log.crud, mdl_logstore_standard_log.edulevel, mdl_logstore_standard_log.ip, mdl_logstore_standard_log.other, DATE_FORMAT(FROM_UNIXTIME(mdl_logstore_standard_log.timecreated),'%Y-%m-%d %H:%i') AS timecreated, mdl_logstore_standard_log.origin, mdl_logstore_standard_log.userid, mdl_user.username, mdl_user.idnumber, mdl_user.firstname, mdl_user.lastname, mdl_user.email, mdl_course.id, mdl_course.fullname , mdl_course.shortname , mdl_course.idnumber, mdl_course.startdate , mdl_course.enddate , mdl_course.category, mdl_course_categories.name, mdl_course_categories.idnumber, mdl_course_categories.parent, mdl_course_categories.coursecount, mdl_course_categories.depth, mdl_course_categories.path FROM mdl_logstore_standard_log INNER JOIN mdl_course ON  mdl_logstore_standard_log.courseid= mdl_course.id INNER JOIN mdl_course_categories ON  mdl_course.category= mdl_course_categories.id INNER JOIN mdl_user ON  mdl_logstore_standard_log.userid= mdl_user.id WHERE eventname='\\\\core\\\\event\\\\course_viewed'"
        sql1="TRUNCATE TABLE course_viewed"
        sql2="""INSERT INTO `course_viewed` (`id_event`, `eventname`, `component`, `action`, `objecttable`, `objectid`, `crud`, `edulevel`, `ip`, `other`, `timecreated`, `origin`, `userid`, `username`, `idnumber`, `firstname`, `lastname`, `email`, `corseid`, `coursefullname`, `shortname`, `courseidnumber`, `startdate`, `enddate`, `categoryid`, `name`, `categoryidnumber`, `parent`, `coursecount`, `depth`, `path`) VALUES ( %s , %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s, %s, %s, %s, %s, %s, %s,%s);"""

        try:
            resul= self.conexion.select(sql)
            print("course_viewed")
            print(len(resul))
            self.conexion1.truncate(sql1)
            self.conexion1.insert(sql2,resul)
            name='User_loggedin'
            Function.createFile(self,name,resul)
        except:
            print("Error insertUser_loggedin")













