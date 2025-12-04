"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

"""
    Retorne la suma de la segunda columna.

    Rta/
    214
"""

def pregunta_01():
    
    ruta = "files/input/data.csv"
    suma = 0

    archivo = open(ruta, "r")

    for fila in archivo:
        fila = fila.strip()        # quitamos saltos de línea
        numero = int(fila[2])      # segunda columna = posición 2
        suma += numero

    archivo.close()
    print(suma)
    return suma

pregunta_01()