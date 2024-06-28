import random

def generarDatosEmpleados():
    datos=[]
    for i in range(5000):   
        empleado={}
        id=random.randint(300,5000)
        nombre=random.choice(['santiago posada','mauro yepes','camila builes','andres gallego','israel alzate'])
        direccion=random.choice(["calle 10 #50-347 medellin","carrera 20#20-20",'carrera 19#59-10','calle 40#30-30','carrera50#26-29'])
        correo=random.choice(['isra@sura.com','juangalleo@sura.com','andres@sura.com.co','cindy@sura.com.co'])
        salario=random.randint(2200000,10000000)
        nHoras=random.randint(42,46)
        fehcaIngreso=random.choice(['1999-05-10','2005-10-20','2010-03-15','2020-07-23','nan','sin','-'])
        empleado=[id,nombre,direccion,correo,salario,nHoras,fehcaIngreso]
        datos.append(empleado)
    return datos
