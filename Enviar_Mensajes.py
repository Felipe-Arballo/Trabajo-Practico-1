from tkinter import *

def crear_ventana_mensajes(raiz_vieja, cifrado):
    raiz_vieja.destroy()
    global raiz2
    raiz2 = Tk()
    raiz2.title(f"Mensajes con cifrado {cifrado}")
    raiz2.geometry("700x450")
    raiz2.resizable(0,0)
    raiz2.iconbitmap("icono.ico")

    texto_entrada_destinatario = Label(raiz2, text="Ingrese el destinatario")
    texto_entrada_destinatario.config(font=("Arial", 12))
    texto_entrada_destinatario.pack(pady=10)
    entrada_destinatario = Entry(raiz2, bg="pink")
    entrada_destinatario.pack(pady=5)

    boton_destinatario = Button(raiz2, text="Verificar Destinatario", command= lambda: verificar_destinatario(cifrado, entrada_destinatario))
    boton_destinatario.pack(pady=10)
    raiz2.mainloop()
    
def verificar_destinatario(cifrado, entrada_destinatario):
    with open("archivo_datos.csv", "r") as archivo:
        datos = leer_archivo_datos(archivo)
    if entrada_destinatario.get() not in datos.keys():
        resultado = False
        motivo = "El destinatario no esta registrado"
    else:
        resultado = True
        motivo = "Ingrese su mensaje"

    texto_mensaje = Label(raiz2 , text=motivo, name="texto_mensaje")
    texto_mensaje.config(font=("Arial" , 12))
    texto_mensaje.pack(pady=10)
    
    if resultado:
        entrada_mensaje = Entry(raiz2, name="entrada_mensaje")
        entrada_mensaje.config(bg="pink")
        entrada_mensaje.pack()
        if cifrado == "Cesar":
            texto_clave = Label(raiz2 , text="Ingrese la clave",name="texto_clave")
            texto_clave.config(font=("Arial" , 12))
            texto_clave.pack(pady=10)

            entrada_clave = Entry(raiz2, name="entrada_clave")
            entrada_clave.config(bg="pink")
            entrada_clave.pack()

        boton_enviar = Button(raiz2, text="Enviar mensaje",name="boton_enviar", command=lambda: enviar_mensaje(entrada_mensaje, entrada_clave))
        boton_enviar.pack(pady=10)
    return resultado

def enviar_mensaje(entrada_mensaje, entrada_clave):
    mensaje = entrada_mensaje.get()
    clave = entrada_clave.get()
