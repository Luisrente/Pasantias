

class Function():

    conexion= None


    def __init__(self, conexion,conexion1):
        self.conexion= conexion
        self.conexion1= conexion1


    def insertCourse_viewed(self):
        sql="SELECT `id`,`eventname`,`component`,`action`,`crud`,`userid`,`courseid`,from_unixtime(timecreated) AS 'Date' FROM `mdl_logstore_standard_log` WHERE `crud`='c';"
        resul=self.conexion.listt(sql)
        sql1="TRUNCATE TABLE Course_viewed"
        self.conexion1.truncate(sql1)
        sql2="""INSERT INTO `Course_viewed` (`id`, `idevent`, `eventname`, `component`, `action`, `crud`, `userid`, `courseid`, `Date`) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s)"""
        self.conexion1.insert(sql2,resul)

    def insertUser_loggedin(self):
        sql="SELECT `id`,`eventname`,`component`,`action`,`crud`,`userid`,`courseid`,from_unixtime(timecreated) AS 'Date' FROM `mdl_logstore_standard_log` WHERE `crud`='c';"
        resul=self.conexion.listt(sql)
        sql1="TRUNCATE TABLE User_loggedin"
        self.conexion1.truncate(sql1)
        sql2="""INSERT INTO `User_loggedin` (`id`, `idevent`, `eventname`, `component`, `action`, `crud`, `userid`, `courseid`, `Date`) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s)"""
        self.conexion1.insert(sql2,resul)

         











