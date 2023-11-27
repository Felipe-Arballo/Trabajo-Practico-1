from tkinter import *

def ingreso_usuario(raiz1):
    raiz1.destroy()
    global raiz2
    raiz2 = Tk()
    raiz2.title("Identificación para acceso")
    raiz2.geometry("700x450")
    raiz2.resizable(0,0)
    #raiz2.iconbitmap("icono.ico")

    label_ingreso_usuario = Label(raiz2 , text="Ingrese su usuario")
    label_ingreso_usuario.config(padx=10 , pady=10 , font=("Arial" , 12))

    entry_ingreso_usuario = Entry(raiz2)
    entry_ingreso_usuario.config(bg="pink")
    entry_ingreso_usuario.place(width=200 , height=40)

    label_ingreso_clave = Label(raiz2 , text="Ingrese su clave")
    label_ingreso_clave.config(padx=10 , pady=10 , font=("Arial" , 12))

    entry_ingreso_clave = Entry(raiz2)
    entry_ingreso_clave.config(bg="pink")
    entry_ingreso_clave.place(width=200 , height=40)

    iniciar_sesion = Button(raiz2 , text="INICIAR SESIÓN")
    iniciar_sesion.config(bg="green" , width=25 , height=2)

    recuperacion_clave = Button(raiz2 , text="Recuperar clave", command=ventana_recuperacion)
    recuperacion_clave.config(bg="red")

    label_ingreso_usuario.pack(pady=10)
    entry_ingreso_usuario.pack(pady=10)
    label_ingreso_clave.pack(pady=10)
    entry_ingreso_clave.pack(pady=10)
    iniciar_sesion.pack(pady=20)
    recuperacion_clave.pack(pady=20)

def verificar_pregunta():
    pregunta_seleccionada = Label(raiz4 , text="Pregunta" , name="pregunta_recuperacion")
    pregunta_seleccionada.pack(pady=10)

    respuesta = Entry(raiz4 , name="respuesta_recuperacion")
    respuesta.pack(pady=10)

    verificar_respuesta = Button(raiz4 , text="Verificar respuesta" , name="verificacion_respuesta_recuperacion")
    verificar_respuesta.config(bg="blue")
    verificar_respuesta.pack(pady=10)

def ventana_recuperacion():
    raiz2.destroy()
    global raiz4
    raiz4 = Tk()
    raiz4.title("Recuperacion Clave")
    raiz4.geometry("700x450")
    raiz4.resizable(0,0)
    raiz4.iconbitmap("icono.ico")

    label_recuperacion_usuario = Label(raiz4 , text="Ingrese su usuario")
    label_recuperacion_usuario.config(padx=10 , pady=10 , font=("Arial" , 12))

    entry_recuperacion_usuario = Entry(raiz4)
    entry_recuperacion_usuario.config(bg="pink")
    entry_recuperacion_usuario.place(width=200 , height=40)

    recuperacion_cuenta = Button(raiz4 , text="RECUPERAR CUENTA" , command = verificar_pregunta)
    recuperacion_cuenta.config(bg="red" , width=25 , height=2)

    label_recuperacion_usuario.pack(pady=10)
    entry_recuperacion_usuario.pack(pady=10)
    recuperacion_cuenta.pack(pady=20)
