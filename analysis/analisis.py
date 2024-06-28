from generators.generadorConsumo import generarDatos

import pandas as pd

def analizarDatos():
    datos=generarDatos()
    tabla=pd.DataFrame(datos,columns=['id','referencia','marca','capacidad','ciudad','consumo','responsable'])
    tabla.to_csv("./data/archivo.csv", index=False)

analizarDatos()