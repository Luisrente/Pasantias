from atexit import register
from connection import Connect
import function 

import mysql.connector as register

register=Connect('localhost',8889,'root','root','Pasas1')


def mainMenu():
    user_loggedin()
    #course_viewed()


def user_loggedin():
    try:
        loggedin=Connect('localhost',8889,'root','root','Pasantia')
        resul=function.listCourse_viewed(loggedin)
        function.insertUser_loggedin(register,resul)
    except:
        print("Error user_loggedin")


def course_viewed():
    course_viewed=Connect('localhost',8889,'root','root','Pasas1')
    resul=function.listCourse_viewed(course_viewed)
    function.insertCourse_viewed(register,resul)

mainMenu()

           

