
from BD.connection1 import DAO1

def list(resultado):
    print(len(resultado))
    dao1=DAO1()
    contador=1
    for cur in resultado:
        #datos= "{0}. Codigo {1} | Nombre: {2} ({3} creditos)"
        #print(datos.format(contador, cur[0], cur[1]))
        dao1.insertLog(cur)
        contador= contador +1 
