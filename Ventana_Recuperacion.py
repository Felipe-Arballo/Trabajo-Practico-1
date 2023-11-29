from tkinter import *

def crear_ventana_recuperacion(raiz_ingreso):
    raiz_ingreso.destroy()
    global raiz_recuperaion
    raiz_recuperaion = Tk()
    raiz_recuperaion.title("Recuperacion Clave")
    raiz_recuperaion.geometry("700x450")
    raiz_recuperaion.resizable(0,0)
    raiz_recuperaion.iconbitmap("icono.ico")

    label_recuperacion_usuario = Label(raiz_recuperaion , text="Ingrese su usuario")
    label_recuperacion_usuario.config(padx=10 , pady=10 , font=("Arial" , 12))

    entry_recuperacion_usuario = Entry(raiz_recuperaion)
    entry_recuperacion_usuario.config(bg="pink")
    entry_recuperacion_usuario.place(width=200 , height=40)

    recuperacion_cuenta = Button(raiz_recuperaion , text="RECUPERAR CUENTA" , command = verificar_pregunta)
    recuperacion_cuenta.config(bg="red" , width=25 , height=2)

    label_recuperacion_usuario.pack(pady=10)
    entry_recuperacion_usuario.pack(pady=10)
    recuperacion_cuenta.pack(pady=20)

def verificar_pregunta():
    pregunta_seleccionada = Label(raiz_recuperaion , text="Pregunta" , name="pregunta_recuperacion")
    pregunta_seleccionada.pack(pady=10)

    respuesta = Entry(raiz_recuperaion , name="respuesta_recuperacion")
    respuesta.pack(pady=10)

    verificar_respuesta = Button(raiz_recuperaion , text="Verificar respuesta" , name="verificacion_respuesta_recuperacion")
    verificar_respuesta.config(bg="blue")
    verificar_respuesta.pack(pady=10)