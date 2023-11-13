from tkinter import*

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

def cifrado_atbash(cadena):
    abecedario = "abcdefghijklmnñopqrstuvwxyz"
    abecedario_invertido = abecedario[::-1]
    numeros = "0123456789"
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

# # Funciones intermedias que señalan errores y mandan los datos a los cifrados (4)
def validar_cesar(entrada_clave, entrada_mensaje):
    if not entrada_clave.get().isnumeric():
        resultado = "CLAVE NO NUMERO"
        devolver_valor(resultado, True)
    clave = int(entrada_clave.get())
    mensaje = entrada_mensaje.get()
    if clave < 0:
        resultado = "CLAVE INVALIDA"
        devolver_valor(resultado, True)
    elif not mensaje: 
        resultado = "FALTA EL MENSAJE"
        devolver_valor(resultado, True)
    else:
        resultado = cifrado_cesar(mensaje,clave)
        devolver_valor(resultado, False)

def validar_cesar2(entrada_clave, entrada_mensaje): 
    if not entrada_clave.get().isnumeric():
        resultado = "CLAVE NO NUMERO"
        devolver_valor(resultado, True)
    clave = -int(entrada_clave.get())
    mensaje = entrada_mensaje.get()
    if clave > 0:
        resultado = "CLAVE INVALIDA"
        devolver_valor(resultado, True)
    elif not mensaje: 
        resultado = "FALTA EL MENSAJE"
        devolver_valor(resultado, True)
    else:
        resultado = cifrado_cesar(mensaje,clave)
        devolver_valor(resultado, False)

def validar_atbash(entrada_mensaje):
    mensaje = entrada_mensaje.get()
    if not mensaje:
        resultado = "FALTA EL MENSAJE"
        devolver_valor(resultado, True)
    else:
        resultado = cifrado_atbash(mensaje)
        devolver_valor(resultado, False)

def crear_ventana_cifrados():
    # # Creamos la segunda ventana (2)
    raiz1.destroy()
    raiz2 = Tk()
    raiz2.title("TP Grupal Parte 1 - Grupo: LOGARITMO")
    raiz2.geometry("700x450")
    raiz2.resizable(0,0)
    raiz2.iconbitmap(r"C:\Users\Usuario\OneDrive\Escritorio\Felipe\Algoritmos y Programación\TP 1\icono.ico")
    
    texto_mensaje = Label(raiz2 , text = "Ingrese el mensaje a cifrar: ")
    texto_mensaje.config(padx=10 , pady=10 , font=("Arial" , 12))
    
    entrada_mensaje = Entry(raiz2)
    entrada_mensaje.config(bg="pink")
    entrada_mensaje.place(width=200 , height=40)
    
    texto_clave = Label(raiz2 , text = "Ingrese la clave del cifrado CESAR: ")
    texto_clave.config(padx=10 , pady=10 , font=("Arial" , 12))
    
    entrada_clave = Entry(raiz2)
    entrada_clave.config(bg="pink")
    entrada_clave.place(width=200 , height=40)
    
    # Ponemos los botones de cifrado y decifrado (3)
    cifrado_CESAR = Button(raiz2 , text="Cifrado CESAR" , bd=10 , relief="ridge" , cursor="hand2" , command=lambda: validar_cesar(entrada_clave, entrada_mensaje))
    
    cifrado_ATBASH = Button(raiz2 , text="Cifrado ATBASH" , bd=10 , relief="ridge" , cursor="hand2" , command=lambda: validar_atbash(entrada_mensaje))
    
    descifrado_CESAR = Button(raiz2 , text="Descifrado CESAR" , bd=10 , relief="ridge" , cursor="hand2" , command=lambda: validar_cesar2(entrada_clave, entrada_mensaje))
    
    descifrado_ATBASH = Button(raiz2 , text="Descifrado ATBASH" , bd=10 , relief="ridge" , cursor="hand2" , command=lambda: validar_atbash(entrada_mensaje))
    
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
    raiz1 = Tk()
    raiz1.title(parametros["ventana_principal"][0])
    raiz1.geometry(parametros["ventana_principal"][1])
    raiz1.resizable(0,0)
    raiz1.iconbitmap(r"C:\Users\Usuario\OneDrive\Escritorio\Felipe\Algoritmos y Programación\TP 1\icono.ico")

    bienvenida = Label(raiz1 , text="Bienvenido a la aplicación de mensajes secretos del grupo LOGARITMO. \n Para continuar presione continuar, de lo contrario cierre la ventana.")
    bienvenida.config(font=("Calibri" , 15) )
    
    continuar = Button(raiz1 , text = "CONTINUAR" , command = crear_ventana_cifrados)
    continuar.config(bg="red" , bd=10 , relief="raised" , font=("Arial" , 15))
    continuar.config(cursor="hand2")
    
    integrantes = Label(raiz1 , text=" \n Construída por: \n - Arballo Felipe Antonio \n - Maldonado Aluhe Nahuel \n - Mancco Puma Osk'r Fabricio \n - Rojas Bravo Diego Ángel \n - Saladino Joaquín")
    integrantes.config(font=("Calibri" , 12))
    
    bienvenida.pack(pady=50)
    continuar.pack(padx=150 , pady=0)
    integrantes.pack(pady=10)
    
    raiz1.mainloop()

def devolver_valor(resultado, error):
    resultado_final = Label(raiz2 , name = "resultado")
    if not error:
            resultado_final.config(bg="grey" , bd=5 , relief="raised" , text="Resultado: " + resultado , width=50 , height=50 , font=("Arial" , 15))
    else:
        resultado_final.config(bg="red" , bd=5 , relief="raised" , text= resultado , width=50 , height=50 , font=("Arial" , 15))
    resultado_final.pack()

# # Funcion que define los parametros de la ventana principal
def definir_parametros():
    parametros = {}
    titulo = "TP Grupal Parte 1 - Grupo: LOGARITMO"
    tamaño = "700x450"
    parametros["ventana_principal"] = (titulo , tamaño)

    tipo_letra_bienvenida = "Calibri"
    tamaño_letra_bienvenida = 15
    parametros["bienvenida_config"] = (tipo_letra_bienvenida , tamaño_letra_bienvenida)

    color_continuar = "red"
    borde_continuar = 10
    tipo_borde_continuar = "raised"
    tipo_cursor = "hand2"
    tipo_letra_continuar = "Arial"
    tamaño_letra_continuar = 15
    parametros["continuar_config"] = (color_continuar, borde_continuar, tipo_borde_continuar, tipo_cursor, tipo_letra_continuar, tamaño_letra_continuar)

    tipo_letra_integrantes = "Calibri"
    tamaño_letra_integrantes = 12
    parametros["integrantes_config"] = (tipo_letra_integrantes, tamaño_letra_integrantes)
    
    return parametros

def definir_parametros_cifrados():
    parametros_cifrados = {}
    
    titulo = "TP Grupal Parte 1 - Grupo: LOGARITMO"
    tamaño = "700x450"
    parametros_cifrados["ventana_cifrados"] = (titulo , tamaño)
    
    tipo_letra_mensaje = "Arial"
    tamaño_letra_mensaje = 12
    parametros_cifrados["mensaje_config"] = (tipo_letra_mensaje , tamaño_letra_mensaje)
    
    color_entrada_mensaje = "pink"
    width_entrada_mensaje = 200
    height_entrada_mensaje = 40
    parametros_cifrados["entrada_mensaje_config"] = (color_entrada_mensaje , width_entrada_mensaje , height_entrada_mensaje)
    
    tipo_letra_clave = "Arial"
    tamaño_letra_clave = 12
    parametros_cifrados["clave_config"] = (tipo_letra_clave , tamaño_letra_clave)
    
    color_entrada_clave = "pink"
    width_entrada_clave = 200
    height_entrada_clave = 40
    parametros_cifrados["entrada_clave_config"] = (color_entrada_clave , width_entrada_clave , height_entrada_clave)
    
    texto_boton_1 = "Cifrado CESAR"
    borde_boton_1 = 10
    relieve_boton_1 = "ridge"
    cursor_boton_1 = "hand2"
    parametros_cifrados["boton_1_config"] = (texto_boton_1 , borde_boton_1 , relieve_boton_1 , cursor_boton_1)
    
    texto_boton_2 = "Cifrado ATBASH"
    borde_boton_2 = 10
    relieve_boton_2 = "ridge"
    cursor_boton_2 = "hand2"
    parametros_cifrados["boton_2_config"] = (texto_boton_2 , borde_boton_2 , relieve_boton_2 , cursor_boton_2)
    
    texto_boton_3 = "Descifrado CESAR"
    borde_boton_3 = 10
    relieve_boton_3 = "ridge"
    cursor_boton_3 = "hand2"
    parametros_cifrados["boton_3_config"] = (texto_boton_3 , borde_boton_3 , relieve_boton_3 , cursor_boton_3)
    
    texto_boton_4 = "Descifrado ATBASH"
    borde_boton_4 = 10
    relieve_boton_4 = "ridge"
    cursor_boton_4 = "hand2"
    parametros_cifrados["boton_4_config"] = (texto_boton_4 , borde_boton_4 , relieve_boton_4 , cursor_boton_4)
    
    return parametros_cifrados

def main():
    crear_ventana_principal(definir_parametros())

main()
