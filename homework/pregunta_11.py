"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """

    archivo = open("files/input/data.csv", "r")
    acumulado = {}

    for linea in archivo:
        partes = linea.split()
        numero = int(partes[1])          # columna 2
        letras_col4 = partes[3].split(",")   # columna 4: lista de letras

        for letra in letras_col4:
            if letra not in acumulado:
                acumulado[letra] = numero
            else:
                acumulado[letra] += numero

    archivo.close()

    # ordenar alfabéticamente y retornar como diccionario
    return dict(sorted(acumulado.items()))