"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    archivo = open("files/input/data.csv", "r")
    conteo_meses = {}

    for fila in archivo:
        partes = fila.split()        # separa columnas por espacios
        fecha = partes[2]            # tercera columna
        mes = fecha.split("-")[1]    # extrae el mes (MM)

        if mes in conteo_meses:
            conteo_meses[mes] += 1
        else:
            conteo_meses[mes] = 1

    archivo.close()

    resultado = sorted(conteo_meses.items())
    return resultado
pregunta_04()