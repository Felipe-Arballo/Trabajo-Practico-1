from tkinter import *

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

def devolver_valor(resultado, error):
    parametros = definir_parametros_resultado()
    raiz2 = Tk()
    resultado_final = Label(raiz2 , name = "#")
    if not error:
            resultado_final.config(bg=parametros["resultado_config"][1] , bd=parametros["resultado_config"][2] , relief=parametros["resultado_config"][3] , text=parametros["resultado_config"][4] + resultado , width=parametros["resultado_config"][5] , height=parametros["resultado_config"][6] , font=(parametros["resultado_config"][7] , parametros["resultado_config"][8]))
    else:
        resultado_final.config(bg=parametros["resultado_config"][0] , bd=parametros["resultado_config"][2] , relief=parametros["resultado_config"][3] , text= resultado , width=parametros["resultado_config"][5] , height=parametros["resultado_config"][6] , font=(parametros["resultado_config"][7] , parametros["resultado_config"][8]))
    resultado_final.pack()

def definir_parametros_resultado():
    parametros = {}
    color_error = "red"
    color_resultado = "grey"
    borde = 5
    relieve = "raised"
    texto = "Resultado:"
    width = 50
    height = 50
    tipo_letra = "Arial"
    tamaño_letra = 15
    parametros["resultado_config"] =(color_error, color_resultado, borde, relieve, texto, width, height, tipo_letra, tamaño_letra)
    return parametros
