abecedario = "abcdefghijklmnñopqrstuvwxyz"
numeros = "0123456789"
clave_no_numero = "CLAVE NO NÚMERO"
clave_invalida = "CLAVE INVÁLIDA"
falta_mensaje = "FALTA EL MENSAJE"

def cifrado_cesar(cadena, clave):
    cadena_modificada = ""
    indice = 0
    while indice < len(cadena):
        letra = cadena[indice]
        if letra.isalnum():
            letra_desplazada = ord(letra) + clave
            cadena_modificada += chr(letra_desplazada)
        else:
            cadena_modificada += letra
        indice += 1
    return cadena_modificada

def cifrado_atbash(cadena):
    abecedario_invertido = abecedario[::-1]
    numeros_invertido = numeros[::-1]
    cadena_codificada = ""
    for letra in cadena:
        if letra.isalpha():
            letra_minuscula = letra.lower()
            indice = abecedario.index(letra_minuscula)
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
