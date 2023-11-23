'''
1. Creación de Usuario
El “Crear Usuario”, deberá desplegar una nueva ventana para poder registrar un usuario, su clave y una
pregunta de seguridad para recuperación de la clave.
El identificador del usuario debe ser validado, sólo puede estar formado por letras, números, y los
caracteres “_” “-” “.”; y tener como mínimo 5 caracteres y como máximo 15. Escribir una función de
validación del identificador del usuario, e incluir al menos 10 casos de prueba significativos.

A su vez, la clave del usuario, deberá tener una longitud de entre 4 y 8 caracteres, formada por al menos
una letra mayúscula, una letra minúscula, un número, y al menos uno de los siguientes caracteres: “_”
“-” “#” “*”. Además, no puede haber caracteres repetidos adyacentes. Escribir una función de
validación de la clave del usuario, e incluir al menos 10 casos de prueba significativos.

La pregunta para recuperación de clave debe poder ser elegida entre las siguientes opciones, que
deberán estar en el archivo preguntas.csv:
1,Apellido de su abuela materna
2,Nombre de tu mascota
3,Nombre de tu mejor amigo/amiga
4,Cantante preferido
5,Ciudad preferida
Deben agregar 5 preguntas más a las existentes al archivo, cada una de las cuales debe estar identificada
por los números del 6 al 10 respectivamente.
Los datos de los usuarios creados deben ser guardados en un archivo csv, cuyo formato debe ser:
Id_usuario,clave_usuario,id_pregunta,respuesta_recuperacion,intentos_recuperacion
En la creación del usuario se debe controlar que el identificador del usuario no exista previamente en el
archivo, en caso de existir, se debe informar “Identificador en uso”
'''

def validar_nombre(nombre):
    longitud = len(nombre)
    simbolos = "_-."
    espacios = " "
    if 5 < longitud < 15 and espacios not in nombre:
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

print(validar_clave("Holac-o0"))




