from conexion import Cone
from function import Function 
import json 

class main:
    def __init__(self):
        ENTORNO= "LOG"
        ENTORNO1="REGISTER"
        with open('./config.json','r') as file:
            config = json.load(file)
        self.conexion= Cone( USER='root',PASS= 'root', HOST= 'localhost' , DB= 'Pasantia', PORT= 8889)
        self.conexion1= Cone( USER='root',PASS= 'root', HOST= 'localhost' , DB= 'Pasas1', PORT= 8889)
        #conexion2= Connect( USER = config[ENTORNO]['PASS'], PASS = config[ENTORNO]['PASS'], HOST = config[ENTORNO]['HOST'], DB = config[ENTORNO]['DATABASE'], PORT = config[ENTORNO]['PORT'])
        #conexion1= Connect(    USER= config[ENTORNO1]['USER']
        #                    , PASS= config[ENTORNO1]['PASS']
        #                    , HOST= config[ENTORNO1]['HOST']
        #                    , DATABASE= config[ENTORNO1]['DATABASE']
        #                    , PORT= config[ENTORNO1]['PORT']
        #                    )
    def execute(self):
        print('Loaing...')
        function=Function(conexion=self.conexion,conexion1=self.conexion1)
        function.insertCourse_viewed()
        function.insertUser_loggedin()

main1=main()
main1.execute()


