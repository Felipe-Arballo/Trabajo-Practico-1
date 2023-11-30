from tkinter import *
from Funciones_Cifrados import leer_archivo_datos

def crear_ventana_recuperacion(raiz_ingreso):
    parametros = parametros_crear_ventana_recuperacion()
    
    raiz_ingreso.destroy()
    global raiz_recuperacion
    raiz_recuperacion = Tk()
    raiz_recuperacion.title(parametros["ventana_crear_usuario"][0])
    raiz_recuperacion.geometry(parametros["ventana_crear_usuario"][1])
    #raiz_recuperacion.iconbitmap(parametros["ventana_crear_usuario"][2])

    label_recuperacion_usuario = Label(raiz_recuperacion , text=parametros["label_recuperar_usuario"][0])
    label_recuperacion_usuario.config(padx=parametros["pads"][0] , pady=parametros["pads"][1] , font=(parametros["label_recuperar_usuario"][1] , parametros["label_recuperar_usuario"][2]))

    entrada_recuperacion_usuario = Entry(raiz_recuperacion)
    entrada_recuperacion_usuario.config(bg=parametros["entry_recuperar_usuario"][0])
    entrada_recuperacion_usuario.place(width=parametros["entry_recuperar_usuario"][1] , height=parametros["entry_recuperar_usuario"][2])

    recuperacion_cuenta = Button(raiz_recuperacion , text=parametros["boton_recuperar_cuenta"][0] , command =lambda:verificar_usuario(entrada_recuperacion_usuario))
    recuperacion_cuenta.config(bg=parametros["boton_recuperar_cuenta"][1] , width=parametros["boton_recuperar_cuenta"][2] , height=parametros["boton_recuperar_cuenta"][3])

    label_recuperacion_usuario.pack(pady=parametros["pads"][1])
    entrada_recuperacion_usuario.pack(pady=parametros["pads"][1])
    recuperacion_cuenta.pack(pady=parametros["pads"][2])
    raiz_recuperacion.mainloop()

def verificar_usuario(entrada_recuperacion_usuario):
    parametros = parametros_verificar_usuario()
    
    usuario = entrada_recuperacion_usuario.get()
    with open("archivo_datos.csv","r") as archivo:
        datos = leer_archivo_datos(archivo)

    if usuario not in datos.keys():
        resultado = False
        motivo = parametros["motivos"]
    else:
        resultado = True
    pregunta_seleccionada = Label(raiz_recuperacion , text=f'{parametros["label_pregunta_seleccionada"][0]} {datos[usuario][3]}' , name=parametros["label_pregunta_seleccionada"][1])
    pregunta_seleccionada.pack(pady=parametros["pads"])

    entrada_respuesta = Entry(raiz_recuperacion , name=parametros["entry_entrada_respuesta"][0])
    entrada_respuesta.config(bg=parametros["entry_entrada_respuesta"][1])
    entrada_respuesta.pack(pady=parametros["pads"])
    
    boton_respuesta = Button(raiz_recuperacion , text=parametros["button_boton_respuesta"][0], name=parametros["button_boton_respuesta"][1], command=lambda: verificar_respuesta(entrada_respuesta, usuario))
    boton_respuesta.config(bg=parametros["button_boton_respuesta"][2])
    boton_respuesta.pack(pady=parametros["pads"])
    return resultado

def verificar_respuesta(entrada_respuesta, usuario):
    parametros = parametros_verificar_respuesta()
    
    with open("archivo_datos.csv","r") as archivo:
        datos = leer_archivo_datos(archivo)
    if datos[usuario][2] != entrada_respuesta.get():
        resultado = False
        motivo = parametros["parametros_verif_rta"][0]
    else:
        resultado = True
        motivo = (f'{parametros["parametros_verif_rta"][1]} {datos[usuario][1]}')
            
    devolver_clave = Label(raiz_recuperacion, text=motivo, name=parametros["parametros_verif_rta"][2])
    devolver_clave.pack(pady=parametros["parametros_verif_rta"][3])
    return resultado

def parametros_crear_ventana_recuperacion():
    diccionario_parametros_crear_ventana_recuperacion = {}
    
    padx_10 = 10
    pady_10 = 10
    pady_20 = 20
    diccionario_parametros_crear_ventana_recuperacion["pads"] = (padx_10 , pady_10 , pady_20)
    
    titulo = "Recuperacion Clave"
    tamaño = "700x450"
    icono = "icono.ico"
    diccionario_parametros_crear_ventana_recuperacion["ventana_crear_usuario"] = (titulo , tamaño , icono)
    
    text_recup_usuario = "Ingrese su usuario"
    tipo_recup_usuario = "Arial"
    tamaño_recup_usuario = 12
    diccionario_parametros_crear_ventana_recuperacion["label_recuperar_usuario"] = (text_recup_usuario , tipo_recup_usuario , tamaño_recup_usuario)
    
    bg_entrada_recuperacion_usuario = "pink"
    width_entrada_recuperacion_usuario = 200
    height_entrada_recuperacion_usuario = 40
    diccionario_parametros_crear_ventana_recuperacion["entry_recuperar_usuario"] = (bg_entrada_recuperacion_usuario , width_entrada_recuperacion_usuario , height_entrada_recuperacion_usuario)
    
    text_recuperacion_cuenta = "RECUPERAR CUENTA"
    bg_recuperacion_cuenta = "red"
    width_recuperacion_cuenta = 25
    height_recuperacion_cuenta = 2
    diccionario_parametros_crear_ventana_recuperacion["boton_recuperar_cuenta"] = (text_recuperacion_cuenta , bg_recuperacion_cuenta , width_recuperacion_cuenta , height_recuperacion_cuenta)
    
    return diccionario_parametros_crear_ventana_recuperacion

def parametros_verificar_usuario():
    diccionario_parametros_verificar_usuario = {}
    
    pady = 10
    diccionario_parametros_verificar_usuario["pads"] = (pady)
    
    motivo_nombre_no_existe = "La cuenta con ese nombre no existe"
    diccionario_parametros_verificar_usuario["motivos"] = (motivo_nombre_no_existe)
    
    text_pregunta_seleccionada = "Pregunta:"
    name_pregunta_seleccionada = "pregunta_recuperacion"
    diccionario_parametros_verificar_usuario["label_pregunta_seleccionada"] = (text_pregunta_seleccionada , name_pregunta_seleccionada)
    
    name_entrada_respuesta = "respuesta_recuperacion"
    bg_entrada_respuesta = "pink"
    diccionario_parametros_verificar_usuario["entry_entrada_respuesta"] = (name_entrada_respuesta , bg_entrada_respuesta)
    
    text_boton_respuesta = "Verificar respuesta"
    name_boton_respuesta = "boton_respuesta"
    bg_boton_respuesta = "red"
    diccionario_parametros_verificar_usuario["button_boton_respuesta"] = (text_boton_respuesta , name_boton_respuesta , bg_boton_respuesta)
    
    return diccionario_parametros_verificar_usuario

def parametros_verificar_respuesta():
    diccionario_parametros_verificar_respuesta = {}
    
    motivo_rta_incorrecta = "Respuesta Incorrecta"
    motivo_su_clave_es = "Su clave es"
    name_devolver_clave = "devolver_clave"
    pady = 10
    diccionario_parametros_verificar_respuesta["parametros_verif_rta"] = (motivo_rta_incorrecta , motivo_su_clave_es , name_devolver_clave , pady)
    
    return diccionario_parametros_verificar_respuesta
