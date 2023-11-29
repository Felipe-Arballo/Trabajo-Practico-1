from tkinter import *
from Funciones_Cifrados import cifrado_atbash , cifrado_cesar, leer_arhivo_mensajes

def consultar_mensajes_cifrados(raiz_vieja):
    global raiz_consulta
    raiz_vieja.destroy()
    raiz_consulta = Tk()
    raiz_consulta.title("Consultar Mensajes Cifrados")
    raiz_consulta.geometry("1000x500")
    raiz_consulta.iconbitmap("icono.ico")
    
    with open("mensajes_enviados.csv", "r") as archivo:
        lineas = leer_arhivo_mensajes(archivo)
    mensajes = []
    for linea in lineas:
        destinatario,remitente,tipo_cifrado,mensaje_cifrado = linea
        if destinatario == "usuario":
            if tipo_cifrado == "A":
                mensaje_descifrado = cifrado_atbash(mensaje_cifrado)
            elif tipo_cifrado[0] == "C":
                mensaje_descifrado = cifrado_cesar(mensaje_cifrado , -(int(tipo_cifrado[1])))
            else:
                mensaje_descifrado = "ERROR"
            resultado = (remitente,mensaje_descifrado)
            mensajes.append(resultado)
    mensajes_ordenados = sorted(mensajes , key=lambda x:x[0])

    texto_lista_mensajes = Label(raiz_consulta , text="Lista de Mensajes:")
    texto_lista_mensajes.config(font=("Arial",15))
    texto_lista_mensajes.pack(anchor="nw")
    
    for lista in mensajes_ordenados:
        separador1 = Label(raiz_consulta , text=(f'{("-"*80)}'))
        separador1.config(font=("Arial",20))
        separador1.pack(anchor="w")
        
        mensajes_recibidos = Label(raiz_consulta , text=(f'{lista[0]}: {lista[1]}'))
        mensajes_recibidos.config(font=("Arial",12))
        mensajes_recibidos.pack(anchor="w")
    
    separador2 = Label(raiz_consulta , text=(f'{("-"*80)}'))
    separador2.config(font=("Arial",20))
    separador2.pack(anchor="w")
    
    cantidad_de_lineas = len(mensajes)
    total_mensajes = Label(raiz_consulta , text=(f'Total de Mensajes: {cantidad_de_lineas}'))
    total_mensajes.config(font=("Arial",15))
    total_mensajes.pack(anchor="w")
    
    raiz_consulta.mainloop()
