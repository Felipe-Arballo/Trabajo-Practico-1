from tkinter import *
from Funciones_Validar import validar_clave, validar_nombre
from Funciones_Cifrados import leer_linea, leer_archivo_datos

def creo_usuario(raiz1):
    parametros = parametros_creo_usuario()
    global raiz3
    raiz1.destroy()
    raiz3 = Tk()
    raiz3.title(parametros["ventana_crear_usuario"][0])
    raiz3.geometry(parametros["ventana_crear_usuario"][1])
    #raiz3.iconbitmap(parametros["ventana_crear_usuario"][2])
    
    texto_usuario = Label(raiz3, text=parametros["label_usuario"][0])
    texto_usuario.config(font=(parametros["label_usuario"][1], parametros["label_usuario"][2]))
    texto_usuario.pack(pady=parametros["pad_y"])

    entrada_usuario = Entry(raiz3)
    entrada_usuario.config(bg=parametros["entry_usuario"])
    entrada_usuario.pack(pady=parametros["pad_y"])

    texto_clave = Label(raiz3, text=parametros["label_clave"][0])
    texto_clave.config(font=(parametros["label_clave"][1], parametros["label_clave"][2]))
    texto_clave.pack(pady=parametros["pad_y"])

    entrada_clave = Entry(raiz3)
    entrada_clave.config(bg=parametros["entry_clave"])
    entrada_clave.pack(pady=parametros["pad_y"])
    with open("preguntas_seguridad.csv", "r") as archivo:
        numero, pregunta = leer_linea(archivo)
        while numero != " ":
            boton_preguntas = Button(raiz3, text=pregunta, command=lambda pregunta=pregunta: seleccionar_pregunta(entrada_usuario, entrada_clave, pregunta))
            boton_preguntas.pack(pady=parametros["pad_y"])
            numero, pregunta = leer_linea(archivo)

def seleccionar_pregunta(entrada_usuario, entrada_clave, pregunta):
    parametros = parametros_seleccionar_pregunta()
    
    entrada_pregunta = Entry(raiz3, name=parametros["entry_pregunta"][0])
    entrada_pregunta.config(bg=parametros["entry_pregunta"][1])
    entrada_pregunta.pack(pady=parametros["pad_y"][1])

    pregunta_seleccionada = Label(raiz3, text=(f'{parametros["label_pregunta"][0]} {pregunta}'), name=parametros["label_pregunta"][1])
    pregunta_seleccionada.pack(pady=parametros["pad_y"][1])

    global pregunta_seleccionada_global
    pregunta_seleccionada_global = pregunta

    crear_cuenta = Button(raiz3, text=parametros["boton_crear_cuenta"][0], name=parametros["boton_crear_cuenta"][1], command=lambda: validar_cuenta(entrada_usuario, entrada_clave, entrada_pregunta, pregunta_seleccionada))
    crear_cuenta.pack(pady=parametros["pad_y"][1])

    validacion = Label(raiz3, name=parametros["label_validacion"])
    validacion.pack()

def validar_cuenta(entrada_usuario, entrada_clave, entrada_pregunta, pregunta_seleccionada):
    parametros = parametros_validar_cuenta()
    
    clave_valida = True
    nombre_valido = True
    respuesta_valida = True
    nombre_usado = False
    with open("archivo_datos.csv", "r") as archivo:
        datos = leer_archivo_datos(archivo)
    if entrada_usuario.get() in datos.keys():
        nombre_usado = True
        motivo = parametros["param_validar_cuenta"][0]
    elif not validar_clave(entrada_clave.get()):
        clave_valida = False
        motivo = parametros["param_validar_cuenta"][1]
    elif not validar_nombre(entrada_usuario.get()):
        nombre_valido = False
        motivo = parametros["param_validar_cuenta"][2]
    elif entrada_pregunta.get() == "":
        respuesta_valida = False
        motivo = parametros["param_validar_cuenta"][3]

    if clave_valida and nombre_valido and respuesta_valida and not nombre_usado:
        guardar_archivo(entrada_usuario, entrada_clave, entrada_pregunta, pregunta_seleccionada)
        validacion = Label(raiz3, text=parametros["param_validar_cuenta"][4], name=parametros["param_validar_cuenta"][6])
        resultado = True
    else:
        validacion = Label(raiz3, text=(f'{parametros["param_validar_cuenta"][5]} {motivo}'), name=parametros["param_validar_cuenta"][6])
        resultado = False
    validacion.pack(pady=parametros["param_validar_cuenta"][7])
    return resultado
    
def guardar_archivo(entrada_usuario, entrada_clave, entrada_pregunta, pregunta_seleccionada):
    with open("archivo_datos.csv", "a") as archivo_datos:
        archivo_datos.write(f'{entrada_usuario.get()},{entrada_clave.get()},{entrada_pregunta.get()},{pregunta_seleccionada_global},{0}\n')

def parametros_creo_usuario():
    diccionario_parametros_creo_usuario = {}

    pad_y_5 = 5
    diccionario_parametros_creo_usuario["pad_y"] = (pad_y_5)
    
    titulo = "TP Grupal Parte 1 - Grupo: LOGARITMO"
    tamaño = "700x650"
    icono = "icono.ico"
    diccionario_parametros_creo_usuario["ventana_crear_usuario"] = (titulo , tamaño , icono)
    
    texto_usuario = "Ingrese el nombre de usuario"
    tipo_letra_usuario = "Arial"
    tamaño_letra_usuario = 10
    diccionario_parametros_creo_usuario["label_usuario"] = (texto_usuario , tipo_letra_usuario , tamaño_letra_usuario)
    
    bg_entry_usuario = "pink"
    diccionario_parametros_creo_usuario["entry_usuario"] = (bg_entry_usuario)
    
    texto_clave = "Ingrese la contraseña"
    tipo_letra_clave = "Arial"
    tamaño_letra_clave = 10
    diccionario_parametros_creo_usuario["label_clave"] = (texto_clave , tipo_letra_clave , tamaño_letra_clave)
    
    bg_entry_clave = "pink"
    diccionario_parametros_creo_usuario["entry_clave"] = (bg_entry_clave)
    
    return diccionario_parametros_creo_usuario
    
def parametros_seleccionar_pregunta():
    diccionario_parametros_seleccionar_pregunta = {}
    
    pad_y_10 = 10
    pad_y_5 = 5
    diccionario_parametros_seleccionar_pregunta["pad_y"] = (pad_y_10 , pad_y_5)
    
    name_entrada_pregunta = "entrada_pregunta"
    bg_entrada_pregunta = "pink"
    diccionario_parametros_seleccionar_pregunta["entry_pregunta"] = (name_entrada_pregunta , bg_entrada_pregunta)
    
    text_pregunta_seleccionada = "Seleccionó la pregunta:"
    name_pregunta_seleccionada =  "texto_pregunta"
    diccionario_parametros_seleccionar_pregunta["label_pregunta"] = (text_pregunta_seleccionada , name_pregunta_seleccionada)
    
    text_crear_cuenta = "Crear Cuenta"
    name_crear_cuenta =  "crear"
    diccionario_parametros_seleccionar_pregunta["boton_crear_cuenta"] = (text_crear_cuenta , name_crear_cuenta)
    
    name_validacion = "validacion"
    diccionario_parametros_seleccionar_pregunta["label_validacion"] = (name_validacion)
    
    return diccionario_parametros_seleccionar_pregunta

def parametros_validar_cuenta():
    diccionario_parametros_validar_cuenta = {}
    
    nombre_usado = "Nombre Usado"
    clave_invalida = "Clave invalida"
    nombre_invalido = "Nombre invalido"
    falta_respuesta = "Falta la respuesta"
    validacion_exitosa = "La validación fue exitosa"
    validacion_rechazada = "No se pudo crear la cuenta:"
    name_validacion = "validacion"
    pad_y = 5
    diccionario_parametros_validar_cuenta["param_validar_cuenta"] = (nombre_usado , clave_invalida , nombre_invalido , falta_respuesta , validacion_exitosa , validacion_rechazada , name_validacion , pad_y)
    
    return diccionario_parametros_validar_cuenta
