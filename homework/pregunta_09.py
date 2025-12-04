"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
{'aaa': 13,
    'bbb': 16,
    'ccc': 23,
    'ddd': 23,
    'eee': 15,
    'fff': 20,
    'ggg': 13,
    'hhh': 16,
    'iii': 18,
    'jjj': 18}}

    """
    archivo = open("files/input/data.csv", "r")
    contador = {}

    for linea in archivo:
        columnas = linea.split()
        pares = columnas[4].split(",")   # elementos tipo 'aaa:3'

        for par in pares:
            clave, _ = par.split(":")    # solo necesitamos la clave
            contador[clave] = contador.get(clave, 0) + 1

    archivo.close()

    return dict(sorted(contador.items()))