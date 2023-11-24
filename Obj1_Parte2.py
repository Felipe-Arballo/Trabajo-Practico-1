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

from tkinter import *

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

def crear_ventana_principal(parametros):
    global raiz1
    raiz1 = Tk()
    raiz1.title(parametros["ventana_principal"][0])
    raiz1.geometry(parametros["ventana_principal"][1])
    raiz1.resizable(0,0)
    raiz1.iconbitmap("icono.ico")

    bienvenida = Label(raiz1 , text=parametros["bienvenida_config"][0])
    bienvenida.config(font=(parametros["bienvenida_config"][1], parametros["bienvenida_config"][2]) )
    
    crear_usuario = Button(raiz1 , text="Crear Usuario" , command = lambda: crear_ventana_cifrados(definir_parametros_cifrados()))
    crear_usuario.config(bg=parametros["continuar_config"][0] , bd=parametros["continuar_config"][1], relief=parametros["continuar_config"][2], cursor=parametros["continuar_config"][3], font=((parametros["continuar_config"][4]), parametros["continuar_config"][5]))

    ingresar_usuario = Button(raiz1 , text="Ingresar Usuario" , command = ingreso_usuariodef ingreso_usuario():
    raiz1.destroy()
    global raiz2
    raiz2 = Tk()
    raiz2.title("Identificación para acceso")
    raiz2.geometry("700x450")
    raiz2.resizable(0,0)
    #raiz2.iconbitmap("icono.ico")

    label_ingreso_usuario = Label(raiz2 , text="Ingrese su usuario")
    label_ingreso_usuario.config(padx=10 , pady=10 , font=("Arial" , 12))

    entry_ingreso_usuario = Entry(raiz2)
    entry_ingreso_usuario.config(bg="pink")
    entry_ingreso_usuario.place(width=200 , height=40)

    label_ingreso_clave = Label(raiz2 , text="Ingrese su clave")
    label_ingreso_clave.config(padx=10 , pady=10 , font=("Arial" , 12))

    entry_ingreso_clave = Entry(raiz2)
    entry_ingreso_clave.config(bg="pink")
    entry_ingreso_clave.place(width=200 , height=40)

    iniciar_sesion = Button(raiz2 , text="INICIAR SESIÓN")
    iniciar_sesion.config(bg="green" , width=25 , height=2)

    recuperacion_clave = Button(raiz2 , text="Recuperar clave")
    recuperacion_clave.config(bg="red")

    label_ingreso_usuario.pack(pady=10)
    entry_ingreso_usuario.pack(pady=10)
    label_ingreso_clave.pack(pady=10)
    entry_ingreso_clave.pack(pady=10)
    iniciar_sesion.pack(pady=20)
    recuperacion_clave.pack(pady=20))
    ingresar_usuario.config(bg=parametros["continuar_config"][0] , bd=parametros["continuar_config"][1], relief=parametros["continuar_config"][2], cursor=parametros["continuar_config"][3], font=((parametros["continuar_config"][4]), parametros["continuar_config"][5]))

    integrantes = Label(raiz1 , text=parametros["integrantes_config"][0])
    integrantes.config(font=(parametros["integrantes_config"][1] , parametros["integrantes_config"][2]))

    bienvenida.pack(pady=50)
    crear_usuario.pack(pady=5)
    ingresar_usuario.pack(pady=5)
    integrantes.pack(pady=10)

    raiz1.mainloop()

def crear_usuario():
    global raiz3
    raiz1.destroy()
    raiz3 = Tk()
    raiz3.title("Ventana de Creacion de Usuario")
    raiz3.geometry("700x500")
    raiz3.resizable(0,0)
    raiz3.iconbitmap("icono.ico")

    texto_usuario = Label(raiz3, text="Ingrese el nombre de usuario")
    texto_usuario.config(font=("Arial" , 12))
    texto_usuario.pack(pady=10)

    entrada_usuario = Entry(raiz3)
    entrada_usuario.config(bg="pink")
    entrada_usuario.pack(pady=10)

    texto_clave = Label(raiz3, text="Ingrese la contraseña")
    texto_clave.config(font=("Arial" , 12))
    texto_clave.pack(pady=10)

    entrada_clave = Entry(raiz3)
    entrada_clave.config(bg="pink")
    entrada_clave.pack(pady=10)

    for pregunta in lista:
        preguntas = Button(raiz3, text=pregunta, name=pregunta.lower(), command=lambda: seleccionar_pregunta(entrada_usuario, entrada_clave))
        preguntas.pack(pady=5)
    
def seleccionar_pregunta(entrada_usuario, entrada_clave):
    entrada_pregunta = Entry(raiz3, name="entrada_pregunta")
    entrada_pregunta.config(bg="pink")
    entrada_pregunta.pack(pady=10)

    pregunta_seleccionada = Label(raiz3, text="Selecciono la pregunta: ", name="texto_pregunta")
    pregunta_seleccionada.pack(pady=10)

    crear_cuenta = Button(raiz3, text="Crear Cuenta",name="crear", command=lambda: validar_cuenta(entrada_usuario, entrada_clave))
    crear_cuenta.pack(pady=5)
    validacion = Label(raiz3, name="validacion")
    validacion.pack()

def validar_cuenta(entrada_usuario, entrada_clave):
    if validar_clave(entrada_clave.get()) and validar_nombre(entrada_usuario.get()):
        resultado = True
    else:
        resultado = False
    validacion = Label(raiz3, text=f"La validacion fue: {resultado}", name="validacion")
    validacion.pack(pady=5)
    return resultado

lista = ("Apellido de su abuela materna", "Nombre de tu mascota", "Nombre de tu mejor amigo/amiga", "Cantante preferido", "Ciudad preferida")


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

def ingreso_usuario():
    raiz1.destroy()
    global raiz2
    raiz2 = Tk()
    raiz2.title("Identificación para acceso")
    raiz2.geometry("700x450")
    raiz2.resizable(0,0)
    #raiz2.iconbitmap("icono.ico")

    label_ingreso_usuario = Label(raiz2 , text="Ingrese su usuario")
    label_ingreso_usuario.config(padx=10 , pady=10 , font=("Arial" , 12))

    entry_ingreso_usuario = Entry(raiz2)
    entry_ingreso_usuario.config(bg="pink")
    entry_ingreso_usuario.place(width=200 , height=40)

    label_ingreso_clave = Label(raiz2 , text="Ingrese su clave")
    label_ingreso_clave.config(padx=10 , pady=10 , font=("Arial" , 12))

    entry_ingreso_clave = Entry(raiz2)
    entry_ingreso_clave.config(bg="pink")
    entry_ingreso_clave.place(width=200 , height=40)

    iniciar_sesion = Button(raiz2 , text="INICIAR SESIÓN")
    iniciar_sesion.config(bg="green" , width=25 , height=2)

    recuperacion_clave = Button(raiz2 , text="Recuperar clave")
    recuperacion_clave.config(bg="red")

    label_ingreso_usuario.pack(pady=10)
    entry_ingreso_usuario.pack(pady=10)
    label_ingreso_clave.pack(pady=10)
    entry_ingreso_clave.pack(pady=10)
    iniciar_sesion.pack(pady=20)
    recuperacion_clave.pack(pady=20)

def verificar_pregunta():
    pregunta_seleccionada = Label(raiz4 , text="Pregunta" , name="pregunta_recuperacion")
    pregunta_seleccionada.pack(pady=10)

    respuesta = Entry(raiz4 , name="respuesta_recuperacion")
    respuesta.pack(pady=10)

    verificar_respuesta = Button(raiz4 , text="Verificar respuesta" , name="verificacion_respuesta_recuperacion")
    verificar_respuesta.config(bg="blue")
    verificar_respuesta.pack(pady=10)

def ventana_recuperacion():
    raiz2.destroy()
    global raiz4
    raiz4 = Tk()
    raiz4.title("Recuperacion Clave")
    raiz4.geometry("700x450")
    raiz4.resizable(0,0)
    #raiz4.iconbitmap("icono.ico")

    label_recuperacion_usuario = Label(raiz4 , text="Ingrese su usuario")
    label_recuperacion_usuario.config(padx=10 , pady=10 , font=("Arial" , 12))

    entry_recuperacion_usuario = Entry(raiz4)
    entry_recuperacion_usuario.config(bg="pink")
    entry_recuperacion_usuario.place(width=200 , height=40)

    recuperacion_cuenta = Button(raiz4 , text="RECUPERAR CUENTA" , command = verificar_pregunta)
    recuperacion_cuenta.config(bg="red" , width=25 , height=2)

    label_recuperacion_usuario.pack(pady=10)
    entry_recuperacion_usuario.pack(pady=10)
    recuperacion_cuenta.pack(pady=20)

def main():
    crear_ventana_principal(definir_parametros())

main()

