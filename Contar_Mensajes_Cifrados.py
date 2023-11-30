from tkinter import *
from Funciones_Cifrados import cifrado_atbash , cifrado_cesar, leer_arhivo_mensajes

def consultar_mensajes_cifrados(raiz_vieja, nombre_usuario):
    parametros = parametros_consultar_mensajes_cifrados()
    
    global raiz_consulta
    raiz_vieja.destroy()
    raiz_consulta = Tk()
    raiz_consulta.title(parametros["parametros_raiz"][0])
    raiz_consulta.geometry(parametros["parametros_raiz"][1])
    raiz_consulta.iconbitmap(parametros["parametros_raiz"][2])
    
    with open("mensajes_enviados.csv", "r") as archivo:
        lineas = leer_arhivo_mensajes(archivo)
    mensajes = []
    for linea in lineas:
        destinatario,remitente,tipo_cifrado,mensaje_cifrado = linea
        if destinatario == nombre_usuario or destinatario == "#":
            if destinatario == "#":
                remitente = "#" + remitente
            if tipo_cifrado == parametros["parametros_varios"][0]:
                mensaje_descifrado = cifrado_atbash(mensaje_cifrado)
            elif tipo_cifrado[0] == parametros["parametros_varios"][1]:
                mensaje_descifrado = cifrado_cesar(mensaje_cifrado , -(int(tipo_cifrado[1])))
            else:
                mensaje_descifrado = parametros["parametros_varios"][2]
            resultado = (remitente,mensaje_descifrado)
            mensajes.append(resultado)
        
    mensajes_ordenados = sorted(mensajes , key=lambda x:x[0])

    texto_lista_mensajes = Label(raiz_consulta , text=parametros["parametros_varios"][3])
    texto_lista_mensajes.config(font=(parametros["fuente_y_posiciones"][0],parametros["fuente_y_posiciones"][1]))
    texto_lista_mensajes.pack(anchor=parametros["anchors"][1])
    
    for lista in mensajes_ordenados:
        separador1 = Label(raiz_consulta , text=(f'{(parametros["parametros_varios"][4]*80)}'))
        separador1.config(font=(parametros["fuente_y_posiciones"][0],parametros["fuente_y_posiciones"][2]))
        separador1.pack(anchor=parametros["anchors"][0])
        
        mensajes_recibidos = Label(raiz_consulta , text=(f'{lista[0]}: {lista[1]}'))
        mensajes_recibidos.config(font=(parametros["fuente_y_posiciones"][0],parametros["fuente_y_posiciones"][3]))
        mensajes_recibidos.pack(anchor=parametros["anchors"][0])
    
    separador2 = Label(raiz_consulta , text=(f'{(parametros["parametros_varios"][4]*80)}'))
    separador2.config(font=(parametros["fuente_y_posiciones"][0],parametros["fuente_y_posiciones"][2]))
    separador2.pack(anchor=parametros["anchors"][0])
    
    cantidad_de_lineas = len(mensajes)
    total_mensajes = Label(raiz_consulta , text=(f'{parametros["parametros_varios"][5]} {cantidad_de_lineas}'))
    total_mensajes.config(font=(parametros["fuente_y_posiciones"][0],parametros["fuente_y_posiciones"][1]))
    total_mensajes.pack(anchor=parametros["anchors"][0])
    
    raiz_consulta.mainloop()
    
def parametros_consultar_mensajes_cifrados():
    diccionario_parametros_consultar_mensajes_cifrados = {}
    
    titulo = "Consultar Mensajes Cifrados"
    tamaño = "1000x500"
    icono = "icono.ico"
    diccionario_parametros_consultar_mensajes_cifrados["parametros_raiz"] = (titulo , tamaño , icono)
    
    tipo_cifrado_A = "A"
    tipo_cifrado_C = "C"
    error_mensaje_descifrado = "ERROR"
    text_texto_lista_mensajes = "Lista de Mensajes:"
    guion = "-"
    text_total_mensajes = "Total de Mensajes:"
    diccionario_parametros_consultar_mensajes_cifrados["parametros_varios"] = (tipo_cifrado_A , tipo_cifrado_C , error_mensaje_descifrado , text_texto_lista_mensajes , guion , text_total_mensajes)
    
    fuente = "Arial"
    tamaño_fuente_15 = 15
    tamaño_fuente_20 = 20
    tamaño_fuente_12 = 12
    diccionario_parametros_consultar_mensajes_cifrados["fuente_y_posiciones"] = (fuente , tamaño_fuente_15 , tamaño_fuente_20 , tamaño_fuente_12)
    
    anchor_w = "w"
    anchor_nw = "nw"
    diccionario_parametros_consultar_mensajes_cifrados["anchors"] = (anchor_w , anchor_nw)
    
    return diccionario_parametros_consultar_mensajes_cifrados
