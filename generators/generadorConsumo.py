import random

def generarDatos():
    datos =[]
    for i in range(5000):
        dato={}
        id=random.randint(1,10000)
        referencia=random.choice(['ACH01','ACH22','ACH43'])
        marca=random.choice(['sony','rico','kalley'])
        capacidad=random.randint(100,2000)
        ciudad=random.choice(['itagui','medellin','jardin','pintada',''])
        responsable=random.choice(['santiago posada','mauro yepes','camila builes','andres gallego','israel alzate'])

        dato=[id,referencia,marca,capacidad,ciudad,responsable]
        datos.append(dato)
    return datos
print(generarDatos())