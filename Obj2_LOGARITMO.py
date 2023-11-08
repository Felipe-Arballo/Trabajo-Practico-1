# Objetivo 2: Cifrado Atbash
# Tomamos como precondicion que la cadena sea un str
# En el abecedario usamos la "ñ" y en los numeros empezamos desde el "0"

def cifrado_atbash(cadena):
    abecedario = "abcdefghijklmnñopqrstuvwxyz"
    abecedario_invertido = abecedario[::-1]
    numeros = "0123456789"
    numeros_invertido = numeros[::-1]
    cadena_codificada = ""
    for letra in cadena:
        if letra.isalpha():
            letra_minus = letra.lower()
            indice = abecedario.index(letra_minus)
            if letra.isupper():
                cadena_codificada += abecedario_invertido[indice]
            else:
                cadena_codificada += abecedario_invertido[indice].upper()
        elif letra.isnumeric():
            indice = numeros.index(letra)
            cadena_codificada += numeros_invertido[indice]
        else:
            cadena_codificada += letra
    return cadena_codificada

# print(cifrado_atbash(""))

'''
Funcion hecha por:
    Arballo Felipe Antonio
    Rojas Bravo Diego Angel 
    Saladino Joaquin
'''      

import doctest

def pruebas2():
    '''
    >>> cifrado_atbash("HOLA MUNDO") # Mayusculas
    'sloz ñfnwl'
    >>> cifrado_atbash("hola mundo") # Minusculas
    'SLOZ ÑFNWL'
    >>> cifrado_atbash("0123456789: Num") # Números
    '9876543210: nFÑ'
    >>> cifrado_atbash("123 *#+-") # Simbolos
    '876 *#+-'
    >>> cifrado_atbash("test5")
    'GVHG5'
    >>> cifrado_atbash("TEST6")
    'gvhg3'
    >>> cifrado_atbash("Test :-)")
    'gVHG :-)'
    >>> cifrado_atbash("sloz ñfnwl") # Desencriptado
    'HOLA MUNDO'
    >>> cifrado_atbash(" ") # Cadena de espacio
    ' '
    >>> cifrado_atbash("") # Cadena vacia
    ''
    '''

print(doctest.testmod())

'''
Funcion hecha por:
    Mancco Puma Osk'r Fabricio
    Maldonado Aluhe 
'''
