from tkinter import *
from Funiones_Validar import validar_atbash, validar_cesar, validar_cesar2
from Enviar_Mensajes import crear_ventana_mensajes

def crear_ventana_cifrados(raiz1):
    parametros = definir_parametros_cifrados()
    global raiz2
    raiz1.destroy()
    raiz2 = Tk()
    raiz2.title(parametros["ventana_cifrados"][0])
    raiz2.geometry(parametros["ventana_cifrados"][1])
    raiz2.resizable(0,0)
    raiz2.iconbitmap("icono.ico")

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

    cifrado_CESAR = Button(raiz2 , text=parametros["texto_boton"][0] , bd=parametros["design_boton"][0] , relief=parametros["design_boton"][1] , cursor=parametros["design_boton"][2] , command=lambda: validar_cesar(entrada_clave, entrada_mensaje))

    cifrado_ATBASH = Button(raiz2 , text=parametros["texto_boton"][1] , bd=parametros["design_boton"][0] , relief=parametros["design_boton"][1] , cursor=parametros["design_boton"][2] , command=lambda: validar_atbash(entrada_mensaje))

    descifrado_CESAR = Button(raiz2 , text=parametros["texto_boton"][2] , bd=parametros["design_boton"][0] , relief=parametros["design_boton"][1] , cursor=parametros["design_boton"][2] , command=lambda: validar_cesar2(entrada_clave, entrada_mensaje))

    descifrado_ATBASH = Button(raiz2 , text=parametros["texto_boton"][3] , bd=parametros["design_boton"][0] , relief=parametros["design_boton"][1] , cursor=parametros["design_boton"][2] , command=lambda: validar_atbash(entrada_mensaje))

    enviar_mensaje_cesar = Button(raiz2, text="Enviar Mensaje Cesar", command=lambda: crear_ventana_mensajes(raiz2, "Cesar"))
    enviar_mensaje_atbash = Button(raiz2, text="Enviar Mensaje Atbash", command=lambda: crear_ventana_mensajes(raiz2, "Atbash"))
    
    texto_mensaje.pack()
    entrada_mensaje.pack()
    texto_clave.pack()
    entrada_clave.pack()
    cifrado_CESAR.pack(padx=20 , pady=10)
    cifrado_ATBASH.pack(padx=20 , pady=10)
    descifrado_CESAR.pack(padx=20 , pady=10)
    descifrado_ATBASH.pack(padx=20 , pady=10)
    enviar_mensaje_cesar.pack(side="left",padx=90, pady=5)
    enviar_mensaje_atbash.pack(side="right",padx=90, pady=5)

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
