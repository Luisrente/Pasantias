from BD.connection import DAO
from BD.connection1 import DAO1
import function 


def mainMenu():
    continu=True
    while(continu):
        correctOption=False
        while(not correctOption):
            print("======  MAIN MENU  ======== ")
            print("1.- Generate report Login")
            print("2.- Generate report view")
            print("3.- Generar  report curse")
            print("4.- Close")
            option = int(input("Select a option: "))
            if option <1 or option>4:
                print("Incorret option enter again...")
            elif option == 4:
                continu= False
                print("Thank you")
                break
            else:
                correctOption= True
                executeOption(option)

def executeOption(option):
    dao= DAO()
    dao1=DAO1()

    if option == 1:  
        try:
         log= dao.listLogs()
         dao1.dropTable()
         dao1.createTable()
         function.list(log)
        except:
            print("Error report")
    elif option == 2:
        dao1.insertLog()
        print("fmfmm")
    else:
        print("Incorret Option")


mainMenu()

           

