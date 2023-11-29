from tkinter import *
from Funciones_Cifrados import cifrado_atbash, cifrado_cesar

clave_no_numero = "CLAVE NO NÚMERO"
clave_invalida = "CLAVE INVÁLIDA"
falta_mensaje = "FALTA EL MENSAJE"

def validar_nombre(nombre):
    longitud = len(nombre)
    simbolos = "_-."
    espacios = " "
    if 5 <= longitud <= 15 and espacios not in nombre:
        resultado = True
    else:
        resultado = False
    indice = 0
    while resultado and indice < longitud:
        if not nombre[indice].isalnum():
            if nombre[indice] not in simbolos:
                resultado = False
        indice += 1
    return resultado

def validar_clave(clave):
    longitud = len(clave)
    tiene_mayusculas = False
    tiene_minusculas = False
    tiene_numeros = False
    tiene_simbolos = False
    simbolos = "_-#*"
    espacios = " "
    if 4 <= longitud <= 8 and espacios not in clave:
        resultado = True
    else:
        resultado = False
    indice = 0
    while resultado and indice < longitud:
        if indice != longitud - 1 and clave[indice] == clave[indice + 1]:
            resultado = False
        elif clave[indice].isupper():
            tiene_mayusculas = True
        elif clave[indice].islower():
            tiene_minusculas = True
        elif clave[indice].isnumeric():
            tiene_numeros = True
        elif clave[indice] in simbolos:
            tiene_simbolos = True
        else:
            resultado = False
        indice += 1
    if resultado and tiene_mayusculas and tiene_minusculas and tiene_numeros and tiene_simbolos:
        resultado_final = True
    else:
        resultado_final = False
    return resultado_final

def validar_cesar(raiz2, entrada_clave, entrada_mensaje):
    if not entrada_clave.get().isnumeric():
        mensaje_descifrado = clave_no_numero
        resultado = False
    clave = -int(entrada_clave.get())
    mensaje = entrada_mensaje.get()
    if clave > 0:
        mensaje_descifrado = clave_invalida
        resultado = False
    elif not mensaje: 
        mensaje_descifrado = falta_mensaje
        resultado = False
    else:
        mensaje_descifrado = cifrado_cesar(mensaje,int(clave))
        resultado = True
    devolver_valor(mensaje_descifrado, resultado, raiz2)
    return resultado

def validar_cesar2(raiz2, entrada_clave, entrada_mensaje): 
    if not entrada_clave.get().isnumeric():
        mensaje_descifrado = clave_no_numero
        resultado = False
    clave = -int(entrada_clave.get())
    mensaje = entrada_mensaje.get()
    if clave > 0:
        mensaje_descifrado = clave_invalida
        resultado = False
    elif not mensaje: 
        mensaje_descifrado = falta_mensaje
        resultado = False
    else:
        mensaje_descifrado = cifrado_cesar(mensaje,-int(clave))
        resultado = True
    devolver_valor(mensaje_descifrado, resultado, raiz2)
    return resultado

def validar_atbash(raiz2, entrada_mensaje):
    mensaje = entrada_mensaje.get()
    if not mensaje:
        mensaje_descifrado = falta_mensaje
        resultado = False
    else:
        mensaje_descifrado = cifrado_atbash(mensaje)
        resultado = True
    devolver_valor(mensaje_descifrado, resultado,raiz2)
    return resultado

def devolver_valor(resultado, validacion, raiz2):
    parametros = definir_parametros_resultado()
    resultado_final = Label(raiz2 , name = "#")
    if validacion:
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
