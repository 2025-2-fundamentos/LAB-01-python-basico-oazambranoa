"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    archivo = open("files/input/data.csv", "r")
    conteo = {}

    for fila in archivo:
        elementos = fila.split()      # separa por espacios
        letra = elementos[0]          # primera columna

        if letra in conteo:
            conteo[letra] += 1
        else:
            conteo[letra] = 1

    archivo.close()

    resultado = sorted(conteo.items())
    return resultado

pregunta_02()