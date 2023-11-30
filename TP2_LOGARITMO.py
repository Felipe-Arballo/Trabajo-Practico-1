from tkinter import *
from Ventana_Crear_Usuario import creo_usuario
from Ventana_Ingresar_Usuario import ingreso_usuario

def crear_ventana_principal(parametros):
    global raiz1
    raiz1 = Tk()
    raiz1.title(parametros["ventana_principal"][0])
    raiz1.geometry(parametros["ventana_principal"][1])
    raiz1.resizable(0,0)
    raiz1.iconbitmap(parametros["ventana_principal"][2])

    bienvenida = Label(raiz1 , text=parametros["bienvenida_config"][0])
    bienvenida.config(font=(parametros["bienvenida_config"][1], parametros["bienvenida_config"][2]))
    
    crear_boton = Button(raiz1 , text=parametros["continuar_config"][6] , command = lambda: creo_usuario(raiz1))
    crear_boton.config(bg=parametros["continuar_config"][0] , bd=parametros["continuar_config"][1], relief=parametros["continuar_config"][2], cursor=parametros["continuar_config"][3], font=((parametros["continuar_config"][4]), parametros["continuar_config"][5]))

    ingresar_boton = Button(raiz1 , text=parametros["continuar_config"][7] , command = lambda: ingreso_usuario(raiz1))
    ingresar_boton.config(bg=parametros["continuar_config"][0] , bd=parametros["continuar_config"][1], relief=parametros["continuar_config"][2], cursor=parametros["continuar_config"][3], font=((parametros["continuar_config"][4]), parametros["continuar_config"][5]))

    integrantes = Label(raiz1 , text=parametros["integrantes_config"][0])
    integrantes.config(font=(parametros["integrantes_config"][1] , parametros["integrantes_config"][2]))

    bienvenida.pack(pady=50)
    crear_boton.pack(pady=5)
    ingresar_boton.pack(pady=5)
    integrantes.pack(pady=10)

    raiz1.mainloop()

def definir_parametros():
    parametros = {}

    titulo = "TP Grupal Parte 1 - Grupo: LOGARITMO"
    tamaño = "700x450"
    icono = "icono.ico"
    parametros["ventana_principal"] = (titulo , tamaño , icono)

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
    texto_crear = "Crear Usuario"
    texto_ingresar = "Ingresar Usuario"
    parametros["continuar_config"] = (color_continuar, borde_continuar, tipo_borde_continuar, tipo_cursor, tipo_letra_continuar, tamaño_letra_continuar, texto_crear, texto_ingresar)

    texto_integrantes = " \n Construída por: \n - Arballo Felipe Antonio \n - Maldonado Aluhe Nahuel \n - Mancco Puma Osk'r Fabricio \n - Rojas Bravo Diego Ángel \n - Saladino Joaquín"
    tipo_letra_integrantes = "Calibri"
    tamaño_letra_integrantes = 12
    parametros["integrantes_config"] = (texto_integrantes, tipo_letra_integrantes, tamaño_letra_integrantes)

    return parametros

def main():
    crear_ventana_principal(definir_parametros())

main()

# # Archivos:
# Revisar la pregunta del archivo al recuperar la cuenta $ Aumentar el contador de veces que se recupero

# # Parametros:
# Ventana recuperacion(verificar_usuario)
# Ventana ingresar_usuario
# Enviar_mensajes
# Contar_mensajes_cifrados
