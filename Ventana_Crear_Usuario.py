from tkinter import *
from Funciones_Validar import validar_clave, validar_nombre

def creo_usuario(raiz1):
    global raiz3
    raiz1.destroy()
    raiz3 = Tk()
    raiz3.title("Ventana de Creacion de Usuario")
    raiz3.geometry("700x500")
    raiz3.resizable(0,0)
    raiz3.iconbitmap("icono.ico")

    texto_usuario = Label(raiz3, text="Ingrese el nombre de usuario")
    texto_usuario.config(font=("Arial" , 12))
    texto_usuario.pack(pady=10)

    entrada_usuario = Entry(raiz3)
    entrada_usuario.config(bg="pink")
    entrada_usuario.pack(pady=10)

    texto_clave = Label(raiz3, text="Ingrese la contraseña")
    texto_clave.config(font=("Arial" , 12))
    texto_clave.pack(pady=10)

    entrada_clave = Entry(raiz3)
    entrada_clave.config(bg="pink")
    entrada_clave.pack(pady=10)

    for pregunta in lista:
        preguntas = Button(raiz3, text=pregunta, name=pregunta.lower(), command=lambda: seleccionar_pregunta(entrada_usuario, entrada_clave))
        preguntas.pack(pady=5)
    
def seleccionar_pregunta(entrada_usuario, entrada_clave):
    entrada_pregunta = Entry(raiz3, name="entrada_pregunta")
    entrada_pregunta.config(bg="pink")
    entrada_pregunta.pack(pady=10)

    pregunta_seleccionada = Label(raiz3, text="Selecciono la pregunta: ", name="texto_pregunta")
    pregunta_seleccionada.pack(pady=10)

    crear_cuenta = Button(raiz3, text="Crear Cuenta",name="crear", command=lambda: validar_cuenta(entrada_usuario, entrada_clave))
    crear_cuenta.pack(pady=5)
    validacion = Label(raiz3, name="validacion")
    validacion.pack()

def validar_cuenta(entrada_usuario, entrada_clave):
    if validar_clave(entrada_clave.get()) and validar_nombre(entrada_usuario.get()):
        resultado = True
    else:
        resultado = False
    validacion = Label(raiz3, text=f"La validacion fue: {resultado}", name="validacion")
    validacion.pack(pady=5)
    return resultado

lista = ("Apellido de su abuela materna", "Nombre de tu mascota", "Nombre de tu mejor amigo/amiga", "Cantante preferido", "Ciudad preferida")
