from generators.generadorEmpleado import generarDatosEmpleados
import pandas as pd

def analizarDatosEmpleados():   
    datos=generarDatosEmpleados()
    tabla=pd.DataFrame(datos,columns=['id','nombre','direccion','correo','salario','nHoras','fehcaIngreso'])
    tabla.to_csv("./data/empleados.csv", index=False)

analizarDatosEmpleados()
