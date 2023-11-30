from tkinter import *
from Ventana_Cifrados import crear_ventana_cifrados
from Ventana_Recuperacion import crear_ventana_recuperacion
from Funciones_Cifrados import leer_archivo_datos

def ingreso_usuario(raiz_vieja):
    parametros = parametros_ingreso_usuario()
    
    raiz_vieja.destroy()
    global raiz_ingreso
    raiz_ingreso = Tk()
    raiz_ingreso.title(parametros["parametros_raiz"][0])
    raiz_ingreso.geometry(parametros["parametros_raiz"][1])
    raiz_ingreso.iconbitmap(parametros["parametros_raiz"][2])

    label_ingreso_usuario = Label(raiz_ingreso , text=parametros["textos"][0])
    label_ingreso_usuario.config(padx=parametros["pads"][0] , pady=parametros["pads"][1] , font=(parametros["fuente_y_tamaño"][0] , parametros["fuente_y_tamaño"][1]))

    entry_ingreso_usuario = Entry(raiz_ingreso)
    entry_ingreso_usuario.config(bg=parametros["backgrounds"][0])
    entry_ingreso_usuario.place(width=parametros["medidas"][0] , height=parametros["medidas"][1])

    label_ingreso_clave = Label(raiz_ingreso , text=parametros["textos"][1])
    label_ingreso_clave.config(padx=parametros["pads"][0] , pady=parametros["pads"][1] , font=(parametros["fuente_y_tamaño"][0] , parametros["fuente_y_tamaño"][1]))

    entry_ingreso_clave = Entry(raiz_ingreso)
    entry_ingreso_clave.config(bg=parametros["backgrounds"][0])
    entry_ingreso_clave.place(width=parametros["medidas"][0] , height=parametros["medidas"][1])

    iniciar_sesion = Button(raiz_ingreso, text=parametros["textos"][2], command=lambda: verificar_cuenta(entry_ingreso_usuario,entry_ingreso_clave))
    iniciar_sesion.config(bg=parametros["backgrounds"][2] , width=parametros["medidas"][2] , height=parametros["medidas"][3])

    recuperacion_clave = Button(raiz_ingreso, text=parametros["textos"][3], command=lambda: crear_ventana_recuperacion(raiz_ingreso))
    recuperacion_clave.config(bg=parametros["backgrounds"][1])

    label_ingreso_usuario.pack(pady=parametros["pads"][1])
    entry_ingreso_usuario.pack(pady=parametros["pads"][1])
    label_ingreso_clave.pack(pady=parametros["pads"][1])
    entry_ingreso_clave.pack(pady=parametros["pads"][1])
    iniciar_sesion.pack(pady=parametros["pads"][2])
    recuperacion_clave.pack(pady=parametros["pads"][2])
    raiz_ingreso.mainloop()

def verificar_cuenta(entrada_usuario,entrada_clave):
    parametros = parametros_verificar_cuenta()
    
    usuario = entrada_usuario.get()
    clave = entrada_clave.get()
    with open("archivo_datos.csv", "r") as archivo:
        datos = leer_archivo_datos(archivo)
    if not usuario in datos.keys():
        resultado = False
        motivo = parametros["parametros_generales"][0]
    elif not datos[usuario][1] == clave:
        resultado = False
        motivo = parametros["parametros_generales"][1]
    else:
        resultado = True
    if resultado:
        crear_ventana_cifrados(raiz_ingreso, usuario)
    else:
        validacion = Label(raiz_ingreso,text=motivo, name=parametros["parametros_generales"][2])
        validacion.pack(pady=parametros["parametros_generales"][3])
    return resultado

def parametros_ingreso_usuario():
    diccionario_parametros_ingreso_usuario = {}
    
    padx_10 = 10
    pady_10 = 10
    pady_20 = 20
    diccionario_parametros_ingreso_usuario["pads"] = (padx_10 , pady_10 , pady_20)
    
    titulo = "Identificación para acceso"
    tamaño = "700x450"
    icono = "icono.ico"
    diccionario_parametros_ingreso_usuario["parametros_raiz"] = (titulo , tamaño , icono)
    
    fuente = "Arial"
    tamaño_fuente = 12
    diccionario_parametros_ingreso_usuario["fuente_y_tamaño"] = (fuente , tamaño_fuente)
    
    bg_pink = "pink"
    bg_red = "red"
    bg_green = "green"
    diccionario_parametros_ingreso_usuario["backgrounds"] = (bg_pink , bg_red , bg_green)
    
    text_label_ingreso_usuario = "Ingrese su usuario"
    text_label_ingreso_clave = "Ingrese su clave"
    text_iniciar_sesion = "INICIAR SESIÓN"
    text_recuperacion_clave = "Recuperar clave"
    diccionario_parametros_ingreso_usuario["textos"] = (text_label_ingreso_usuario , text_label_ingreso_clave , text_iniciar_sesion , text_recuperacion_clave)
    
    width_200 = 200
    height_40 = 40
    width_25 = 25
    height_2 = 2
    diccionario_parametros_ingreso_usuario["medidas"] = (width_200 , height_40 , width_25 , height_2)
    
    return diccionario_parametros_ingreso_usuario

def parametros_verificar_cuenta():
    diccionario_parametros_verificar_cuenta = {}
    
    no_registrado = "Usuario no registrado"
    no_coinciden = "El nombre y la contraseña no coinciden"
    name_validacion = "verificar_cuenta"
    pady_validacion = 5
    diccionario_parametros_verificar_cuenta["parametros_generales"] = (no_registrado , no_coinciden , name_validacion , pady_validacion)
    
    return diccionario_parametros_verificar_cuenta
