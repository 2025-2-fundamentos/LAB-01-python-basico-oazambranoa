"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
    ('bbb', 1, 9),
    ('ccc', 1, 10),
    ('ddd', 0, 9),
    ('eee', 1, 7),
    ('fff', 0, 9),
    ('ggg', 3, 10),
    ('hhh', 0, 9),
    ('iii', 0, 9),
    ('jjj', 5, 17)]

    """
    
    archivo = open("files/input/data.csv", "r")
    acumulado = {}

    for linea in archivo:
        columnas = linea.split()
        pares = columnas[4].split(",")   # columna 5 con formato k:v,k:v,...

        for par in pares:
            clave, numero = par.split(":")
            numero = int(numero)

            if clave not in acumulado:
                # [mínimo, máximo]
                acumulado[clave] = [numero, numero]
            else:
                if numero < acumulado[clave][0]:
                    acumulado[clave][0] = numero
                if numero > acumulado[clave][1]:
                    acumulado[clave][1] = numero

    archivo.close()

    resultado = []
    for clave in acumulado:
        minimo = acumulado[clave][0]
        maximo = acumulado[clave][1]
        resultado.append((clave, minimo, maximo))

    return sorted(resultado)

pregunta_06()