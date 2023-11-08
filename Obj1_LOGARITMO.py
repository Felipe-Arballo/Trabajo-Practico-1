# # Objetivo 1: Cifrado Cesár
# Tomamos como precondicion que la cadena sea un str y la clave un int
# La clave tomamos como que solo mueve para la derecha (clave >= 0)

def cifrado_cesar(cadena, clave):
    cadena_modificada = ""
    if clave < 0:
        resultado = False
        cadena_modificada = "ERROR clave negativa"
    else: 
        resultado = True
    indice = 0
    while resultado and indice < len(cadena):
        letra = cadena[indice]
        if letra.isalnum():
            letra_desplazada = ord(letra) + clave
            cadena_modificada += chr(letra_desplazada)
        else:
            cadena_modificada += letra
        indice += 1
    return cadena_modificada

# print(cifrado_cesar("HOLA MUNDO", 3))

'''
Funcion hecha por:
    Arballo Felipe Antonio
    Rojas Bravo Diego Angel 
    Saladino Joaquin
'''      
import doctest

def pruebas():
    '''
    >>> cifrado_cesar("HOLA MUNDO", 3) # Mayusculas
    'KROD PXQGR'
    >>> cifrado_cesar("hola mundo", 3) # Minusculas
    'krod pxqgr'
    >>> cifrado_cesar("1234567890: NUM", 1) # Numeros
    '23456789:1: OVN'
    >>> cifrado_cesar("hola: -+`¡'!/10", 10) # Simbolos
    "ryvk: -+`¡'!/;:"
    >>> cifrado_cesar("numeros: 192837465", 0) # Clave 0
    'numeros: 192837465'
    >>> cifrado_cesar("HOla MUndo", -3) # Clave negativa
    'ERROR clave negativa'
    >>> cifrado_cesar("ho123l2a num-3 -2", 2)
    'jq345n4c pwo-5 -4'
    >>> cifrado_cesar("HOLA MUNDO", 30000) # Clave muy alta
    '畸畿畼畱 畽疅畾畴畿'
    >>> cifrado_cesar(" ", 2) # Cadena de espacio
    ' '
    >>> cifrado_cesar("", 2) # Cadena vacia
    ''
    '''

print(doctest.testmod())

'''
Funcion hecha por:
    Mancco Puma Osk'r Fabricio
    Maldonado Aluhe 
'''
