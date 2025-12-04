"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    archivo = open("files/input/data.csv", "r")
    estadisticas = {}

    for fila in archivo:
        partes = fila.split()
        letra = partes[0]
        numero = int(partes[1])

        if letra not in estadisticas:
            # inicializamos: (max = numero, min = numero)
            estadisticas[letra] = [letra, numero, numero]
        else:
            # actualizar máximo y mínimo
            if numero > estadisticas[letra][1]:
                estadisticas[letra][1] = numero

            if numero < estadisticas[letra][2]:
                estadisticas[letra][2] = numero

    archivo.close()

    # Convertimos los valores dict a lista de tuplas
    resultado = []
    for clave in estadisticas:
        resultado.append(tuple(estadisticas[clave]))

    return sorted(resultado)

pregunta_05()