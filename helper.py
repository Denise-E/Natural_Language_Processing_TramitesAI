import re

def encontrar_posicion_regex(cadena, palabra):
    patron = re.escape(palabra)  # Escapar palabra para caracteres especiales
    coincidencia = re.search(patron, cadena)
    if coincidencia:
        return (coincidencia.start(), coincidencia.end())
    return None


cadena = None
palabra = None
posicion = encontrar_posicion_regex(cadena, palabra)

print(posicion)