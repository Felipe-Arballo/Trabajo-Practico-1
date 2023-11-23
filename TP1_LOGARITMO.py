from tkinter import*
import doctest

# Strings varios para utilizar luego
abecedario = "abcdefghijklmnñopqrstuvwxyz"
numeros = "0123456789"
clave_no_numero = "CLAVE NO NÚMERO"
clave_invalida = "CLAVE INVÁLIDA"
falta_mensaje = "FALTA EL MENSAJE"

# # Importamos tkinter y debajo estan los cifrados de los objetivos anterirores
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

def pruebas_CESAR():
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
    >>> cifrado_cesar("ho123l2a num-3 -2", 2)
    'jq345n4c pwo-5 -4'
    >>> cifrado_cesar("h0l@ & ad10$" , 3) # Letras, numeros y simbolos
    'k3o@ & dg43$'
    >>> cifrado_cesar("HOLA MUNDO", 30000) # Clave muy alta
    '畸畿畼畱 畽疅畾畴畿'
    >>> cifrado_cesar(" ", 2) # Cadena de espacio
    ' '
    >>> cifrado_cesar("", 2) # Cadena vacia
    ''
    '''

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

def pruebas_ATBASH():
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

# print(doctest.testmod())

# # Funciones intermedias que señalan errores y mandan los datos a los cifrados (4)
def validar_cesar(entrada_clave, entrada_mensaje):
    if not entrada_clave.get().isnumeric():
        resultado = clave_no_numero
        devolver_valor(resultado, True)
    clave = int(entrada_clave.get())
    mensaje = entrada_mensaje.get()
    if clave < 0:
        resultado = clave_invalida
        devolver_valor(resultado, True)
    elif not mensaje: 
        resultado = falta_mensaje
        devolver_valor(resultado, True)
    else:
        resultado = cifrado_cesar(mensaje,clave)
        devolver_valor(resultado, False)

def validar_cesar2(entrada_clave, entrada_mensaje): 
    if not entrada_clave.get().isnumeric():
        resultado = clave_no_numero
        devolver_valor(resultado, True)
    clave = -int(entrada_clave.get())
    mensaje = entrada_mensaje.get()
    if clave > 0:
        resultado = clave_invalida
        devolver_valor(resultado, True)
    elif not mensaje: 
        resultado = falta_mensaje
        devolver_valor(resultado, True)
    else:
        resultado = cifrado_cesar(mensaje,clave)
        devolver_valor(resultado, False)

def validar_atbash(entrada_mensaje):
    mensaje = entrada_mensaje.get()
    if not mensaje:
        resultado = falta_mensaje
        devolver_valor(resultado, True)
    else:
        resultado = cifrado_atbash(mensaje)
        devolver_valor(resultado, False)

def crear_ventana_cifrados(parametros):
    # # Creamos la segunda ventana (2)
    global raiz2
    raiz1.destroy()
    raiz2 = Tk()
    raiz2.title(parametros["ventana_cifrados"][0])
    raiz2.geometry(parametros["ventana_cifrados"][1])
    raiz2.resizable(0,0)
    raiz2.iconbitmap("TP1_LOGARITMO//icono.ico")

    texto_mensaje = Label(raiz2 , text=parametros["mensaje_config"][0])
    texto_mensaje.config(padx=10 , pady=10 , font=(parametros["mensaje_config"][1] , parametros["mensaje_config"][2]))

    entrada_mensaje = Entry(raiz2)
    entrada_mensaje.config(bg=parametros["entrada_mensaje_config"][0])
    entrada_mensaje.place(width=parametros["entrada_mensaje_config"][1] , height=parametros["entrada_mensaje_config"][2])

    texto_clave = Label(raiz2 , text=parametros["clave_config"][0])
    texto_clave.config(padx=10 , pady=10 , font=(parametros["clave_config"][1] , parametros["clave_config"][2]))

    entrada_clave = Entry(raiz2)
    entrada_clave.config(bg=parametros["entrada_clave_config"][0])
    entrada_clave.place(width=parametros["entrada_clave_config"][1] , height=parametros["entrada_clave_config"][2])

    # Ponemos los botones de cifrado y descifrado (3)

    cifrado_CESAR = Button(raiz2 , text=parametros["texto_boton"][0] , bd=parametros["design_boton"][0] , relief=parametros["design_boton"][1] , cursor=parametros["design_boton"][2] , command=lambda: validar_cesar(entrada_clave, entrada_mensaje))

    cifrado_ATBASH = Button(raiz2 , text=parametros["texto_boton"][1] , bd=parametros["design_boton"][0] , relief=parametros["design_boton"][1] , cursor=parametros["design_boton"][2] , command=lambda: validar_atbash(entrada_mensaje))

    descifrado_CESAR = Button(raiz2 , text=parametros["texto_boton"][2] , bd=parametros["design_boton"][0] , relief=parametros["design_boton"][1] , cursor=parametros["design_boton"][2] , command=lambda: validar_cesar2(entrada_clave, entrada_mensaje))

    descifrado_ATBASH = Button(raiz2 , text=parametros["texto_boton"][3] , bd=parametros["design_boton"][0] , relief=parametros["design_boton"][1] , cursor=parametros["design_boton"][2] , command=lambda: validar_atbash(entrada_mensaje))

    texto_mensaje.pack()
    entrada_mensaje.pack()
    texto_clave.pack()
    entrada_clave.pack()
    cifrado_CESAR.pack(padx=20 , pady=15)
    cifrado_ATBASH.pack(padx=20 , pady=15)
    descifrado_CESAR.pack(padx=20 , pady=15)
    descifrado_ATBASH.pack(padx=20 , pady=15)

# # Creamos la primer ventana (1)
# Cuando recibe la funcion los parametros los usamos asi? (parametros["ventana_principal"][0]) o les damos nombre primero?
def crear_ventana_principal(parametros):
    global raiz1
    raiz1 = Tk()
    raiz1.title(parametros["ventana_principal"][0])
    raiz1.geometry(parametros["ventana_principal"][1])
    raiz1.resizable(0,0)
    raiz1.iconbitmap("TP1_LOGARITMO//icono.ico")

    bienvenida = Label(raiz1 , text=parametros["bienvenida_config"][0])
    bienvenida.config(font=(parametros["bienvenida_config"][1], parametros["bienvenida_config"][2]) )
    
    continuar = Button(raiz1 , text=parametros["continuar_config"][6] , command = lambda: crear_ventana_cifrados(definir_parametros_cifrados()))
    continuar.config(bg=parametros["continuar_config"][0] , bd=parametros["continuar_config"][1], relief=parametros["continuar_config"][2], cursor=parametros["continuar_config"][3], font=((parametros["continuar_config"][4]), parametros["continuar_config"][5]))

    integrantes = Label(raiz1 , text=parametros["integrantes_config"][0])
    integrantes.config(font=(parametros["integrantes_config"][1] , parametros["integrantes_config"][2]))

    bienvenida.pack(pady=50)
    continuar.pack(padx=150 , pady=0)
    integrantes.pack(pady=10)

    raiz1.mainloop()

def devolver_valor(resultado, error):
    parametros = definir_parametros_resultado()
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
    
# # Funcion que define los parametros de la ventana principal
def definir_parametros():
    parametros = {}

    titulo = "TP Grupal Parte 1 - Grupo: LOGARITMO"
    tamaño = "700x450"
    parametros["ventana_principal"] = (titulo , tamaño)

    texto_bienvenida = "Bienvenido a la aplicación de mensajes secretos del grupo LOGARITMO. \n Para continuar presione continuar, de lo contrario cierre la ventana."
    tipo_letra_bienvenida = "Calibri"
    tamaño_letra_bienvenida = 15
    parametros["bienvenida_config"] = (texto_bienvenida, tipo_letra_bienvenida, tamaño_letra_bienvenida)

    color_continuar = "red"
    borde_continuar = 10
    tipo_borde_continuar = "raised"
    tipo_cursor = "hand2"
    tipo_letra_continuar = "Arial"
    tamaño_letra_continuar = 15
    nombre_boton = "CONTINUAR"
    parametros["continuar_config"] = (color_continuar, borde_continuar, tipo_borde_continuar, tipo_cursor, tipo_letra_continuar, tamaño_letra_continuar, nombre_boton)

    texto_integrantes = " \n Construída por: \n - Arballo Felipe Antonio \n - Maldonado Aluhe Nahuel \n - Mancco Puma Osk'r Fabricio \n - Rojas Bravo Diego Ángel \n - Saladino Joaquín"
    tipo_letra_integrantes = "Calibri"
    tamaño_letra_integrantes = 12
    parametros["integrantes_config"] = (texto_integrantes, tipo_letra_integrantes, tamaño_letra_integrantes)

    return parametros

def definir_parametros_cifrados():
    parametros_cifrados = {}

    titulo = "TP Grupal Parte 1 - Grupo: LOGARITMO"
    tamaño = "700x450"
    parametros_cifrados["ventana_cifrados"] = (titulo , tamaño)

    texto_mensaje = "Ingrese el mensaje a cifrar: "
    tipo_letra_mensaje = "Arial"
    tamaño_letra_mensaje = 12
    parametros_cifrados["mensaje_config"] = (texto_mensaje, tipo_letra_mensaje, tamaño_letra_mensaje)

    color_entrada_mensaje = "pink"
    width_entrada_mensaje = 200
    height_entrada_mensaje = 40
    parametros_cifrados["entrada_mensaje_config"] = (color_entrada_mensaje , width_entrada_mensaje , height_entrada_mensaje)

    texto_clave = "Ingrese la clave del cifrado CESAR: "
    tipo_letra_clave = "Arial"
    tamaño_letra_clave = 12
    parametros_cifrados["clave_config"] = (texto_clave, tipo_letra_clave, tamaño_letra_clave)

    color_entrada_clave = "pink"
    width_entrada_clave = 200
    height_entrada_clave = 40
    parametros_cifrados["entrada_clave_config"] = (color_entrada_clave , width_entrada_clave , height_entrada_clave)

    texto_boton_1 = "Cifrado CESAR"
    texto_boton_2 = "Cifrado ATBASH"
    texto_boton_3 = "Descifrado CESAR"
    texto_boton_4 = "Descifrado ATBASH"
    parametros_cifrados["texto_boton"] = (texto_boton_1 , texto_boton_2 , texto_boton_3 , texto_boton_4)

    borde_boton = 10
    relieve_boton = "ridge"
    cursor_boton = "hand2"
    parametros_cifrados["design_boton"] = (borde_boton , relieve_boton , cursor_boton)

    return parametros_cifrados

def main():
    crear_ventana_principal(definir_parametros())

main()
