"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
        ('A', 3, 4),
        ...
        ('E', 2, 3),
        ('E', 3, 3)]


    """
    archivo = open("files/input/data.csv", "r")
    resultado = []

    for linea in archivo:
        partes = linea.split()

        letra = partes[0]
        lista_col4 = partes[3].split(",")   # columna 4: lista de items
        lista_col5 = partes[4].split(",")   # columna 5: diccionario k:v pero separado por comas

        cantidad_4 = len(lista_col4)
        cantidad_5 = len(lista_col5)

        resultado.append((letra, cantidad_4, cantidad_5))

    archivo.close()
    return resultado