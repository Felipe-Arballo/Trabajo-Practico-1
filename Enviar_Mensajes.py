from tkinter import *
from Funciones_Cifrados import cifrado_atbash, cifrado_cesar, leer_linea
from Funciones_Validar import validar_atbash, validar_cesar

def crear_ventana_mensajes(raiz_vieja, cifrado, nombre_usuario):
    parametros = parametros_crear_ventana_mensajes()
    
    raiz_vieja.destroy()
    global raiz2
    raiz2 = Tk()
    raiz2.title(f'{parametros["parametros_raiz"][0]} {cifrado}')
    raiz2.geometry(parametros["parametros_raiz"][1])
    raiz2.iconbitmap(parametros["parametros_raiz"][2])

    texto_entrada_destinatario = Label(raiz2, text=parametros["parametros_varios"][0])
    texto_entrada_destinatario.config(font=(parametros["fuente_y_pads"][0], parametros["fuente_y_pads"][1]))
    texto_entrada_destinatario.pack(pady=parametros["fuente_y_pads"][3])
    entrada_destinatario = Entry(raiz2, bg=parametros["parametros_varios"][1])
    entrada_destinatario.pack(pady=parametros["fuente_y_pads"][2])

    boton_destinatario = Button(raiz2, text=parametros["parametros_varios"][2], command= lambda: verificar_destinatario(cifrado, entrada_destinatario, nombre_usuario))
    boton_destinatario.pack(pady=parametros["fuente_y_pads"][3])
    raiz2.mainloop()
    
def verificar_destinatario(cifrado, entrada_destinatario, nombre_usuario):
    parametros = parametros_verificar_destinatario()
    resultado = False
    with open("archivo_datos.csv", "r") as archivo:
        linea = leer_linea(archivo)
        while linea[0] != " " and not resultado:
            if linea[0] == entrada_destinatario.get():
                resultado = True
            linea = leer_linea(archivo)

    if resultado:
        mostrar_ventana = parametros["mostrar_ventana"][1]
    else:
        mostrar_ventana = parametros["mostrar_ventana"][0]

    texto_mensaje = Label(raiz2 , text= mostrar_ventana, name=parametros["parametros_varios"][0])
    texto_mensaje.config(font=(parametros["fuente_y_pads"][0] , parametros["fuente_y_pads"][1]))
    texto_mensaje.pack(pady=parametros["fuente_y_pads"][2])
    
    entrada_mensaje = Entry(raiz2, name=parametros["parametros_varios"][1])
    entrada_mensaje.config(bg=parametros["background"])

    boton_enviar = Button(raiz2, text=parametros["parametros_varios"][6],name=parametros["parametros_varios"][7], command=lambda: enviar_mensaje(entrada_mensaje, entrada_clave, entrada_destinatario, nombre_usuario))
        
    if cifrado == parametros["parametros_varios"][2]:
        texto_clave = Label(raiz2 , text=parametros["parametros_varios"][3],name=parametros["parametros_varios"][4])
        texto_clave.config(font=(parametros["fuente_y_pads"][0] , parametros["fuente_y_pads"][1]))
            
        entrada_clave = Entry(raiz2, name=parametros["parametros_varios"][5])
        entrada_clave.config(bg=parametros["background"])
        
        if resultado:
            entrada_mensaje.pack()
            texto_clave.pack(pady=parametros["fuente_y_pads"][2])
            entrada_clave.pack()
            boton_enviar.pack(pady=parametros["fuente_y_pads"][2])
        else:
            entrada_mensaje.grid_remove()
            texto_clave.grid_remove()
            entrada_clave.grid_remove()
            boton_enviar.grid_remove()
    else:
        entrada_clave = "Atbash"
        if resultado:
            entrada_mensaje.pack()
            boton_enviar.pack(pady=parametros["fuente_y_pads"][2])
        else:
            entrada_mensaje.grid_remove()
            boton_enviar.grid_remove()

    return resultado

def enviar_mensaje(entrada_mensaje, entrada_clave, entrada_destinatario, nombre_usuario):
    if entrada_clave != "Atbash":
        tipo_cifrado = "C" + entrada_clave.get()
    else:
        tipo_cifrado = "A"
    
    if tipo_cifrado == "A":
        cifrado_valido = validar_atbash("",entrada_mensaje)
    else:
        cifrado_valido = validar_cesar("",entrada_clave, entrada_mensaje)

    if cifrado_valido:
        mensaje = entrada_mensaje.get()
        destinatario = entrada_destinatario.get()
        if tipo_cifrado == "A":
            mensaje_cifrado = cifrado_atbash(mensaje)
        else:
            clave = int(entrada_clave.get())
            mensaje_cifrado = cifrado_cesar(mensaje, clave)
        mostrar_ventana = "Mensaje Enviado"
        with open("mensajes_enviados.csv", "a") as archivo_mensajes:
            archivo_mensajes.write(f'{destinatario},{nombre_usuario},{tipo_cifrado},{mensaje_cifrado}\n')

    else:
        mostrar_ventana = "Error de validacion"
    
    validacion = Label(raiz2, text=mostrar_ventana, name="validacion")
    validacion.pack()
        
def parametros_crear_ventana_mensajes():
    diccionario_parametros_crear_ventana_mensajes = {}
    
    fuente = "Arial"
    tamaño_fuente = 12
    pady_5 = 5
    pady_10 = 10
    diccionario_parametros_crear_ventana_mensajes["fuente_y_pads"] = (fuente , tamaño_fuente , pady_5 , pady_10)
    
    titulo = "Mensajes con cifrado"
    tamaño = "700x450"
    icono = "icono.ico"
    diccionario_parametros_crear_ventana_mensajes["parametros_raiz"] = (titulo , tamaño , icono)
    
    text_entrada__destinatario = "Ingrese el destinatario"
    bg_entrada_destinatario = "pink"
    text_boton__destinatario = "Verificar Destinatario"
    diccionario_parametros_crear_ventana_mensajes["parametros_varios"] = (text_entrada__destinatario , bg_entrada_destinatario , text_boton__destinatario)
    
    return diccionario_parametros_crear_ventana_mensajes

def parametros_verificar_destinatario():
    diccionario_parametros_verificar_destinatario = {}
    
    fuente = "Arial"
    tamaño_fuente = 12
    pady_10 = 10
    diccionario_parametros_verificar_destinatario["fuente_y_pads"] = (fuente , tamaño_fuente , pady_10)
    
    bg = "pink"
    diccionario_parametros_verificar_destinatario["background"] = (bg)
    
    mostrar_ventana_1 = "El destinatario no esta registrado"
    mostrar_ventana_2 = "Ingrese su mensaje"
    diccionario_parametros_verificar_destinatario["mostrar_ventana"] = (mostrar_ventana_1 , mostrar_ventana_2)
    
    name_texto_mensaje = "texto_mensaje"
    name_entrada_mensaje = "entrada_mensaje"
    si_cifrado_es = "Cesar"
    text_texto_clave = "Ingrese la clave"
    name_texto_clave = "texto_clave"
    name_entrada_clave = "entrada_clave"
    text_boton_enviar = "Enviar mensaje"
    name_boton_enviar = "boton_enviar"
    diccionario_parametros_verificar_destinatario["parametros_varios"] = (name_texto_mensaje , name_entrada_mensaje , si_cifrado_es , text_texto_clave , name_texto_clave , name_entrada_clave , text_boton_enviar , name_boton_enviar)

    return diccionario_parametros_verificar_destinatario
