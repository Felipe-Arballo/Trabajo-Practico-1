from tkinter import *
from Funciones_Validar import validar_clave, validar_nombre
from Funciones_Cifrados import leer_archivo_datos

def creo_usuario(raiz1):
    global raiz3
    raiz1.destroy()
    raiz3 = Tk()
    raiz3.title("Ventana de Creacion de Usuario")
    raiz3.geometry("700x500")
    raiz3.resizable(0, 0)
    #raiz3.iconbitmap("icono.ico")
    
    texto_usuario = Label(raiz3, text="Ingrese el nombre de usuario")
    texto_usuario.config(font=("Arial", 12))
    texto_usuario.pack(pady=10)

    entrada_usuario = Entry(raiz3)
    entrada_usuario.config(bg="pink")
    entrada_usuario.pack(pady=10)

    texto_clave = Label(raiz3, text="Ingrese la contraseña")
    texto_clave.config(font=("Arial", 12))
    texto_clave.pack(pady=10)

    entrada_clave = Entry(raiz3)
    entrada_clave.config(bg="pink")
    entrada_clave.pack(pady=10)
    with open("preguntas_seguridad.csv", "r") as archivo:
        preguntas = leer_archivo_datos(archivo)
        for pregunta in preguntas.values():
            boton_preguntas = Button(raiz3, text=pregunta[1], command=lambda pregunta=pregunta[1]: seleccionar_pregunta(entrada_usuario, entrada_clave, pregunta))
            boton_preguntas.pack(pady=5)

def seleccionar_pregunta(entrada_usuario, entrada_clave, pregunta):
    entrada_pregunta = Entry(raiz3, name="entrada_pregunta")
    entrada_pregunta.config(bg="pink")
    entrada_pregunta.pack(pady=10)

    pregunta_seleccionada = Label(raiz3, text=f"Seleccionó la pregunta: {pregunta}", name="texto_pregunta")
    pregunta_seleccionada.pack(pady=10)

    global pregunta_seleccionada_global
    pregunta_seleccionada_global = pregunta

    crear_cuenta = Button(raiz3, text="Crear Cuenta", name="crear", command=lambda: validar_cuenta(entrada_usuario, entrada_clave, entrada_pregunta, pregunta_seleccionada))
    crear_cuenta.pack(pady=5)

    validacion = Label(raiz3, name="validacion")
    validacion.pack()

def validar_cuenta(entrada_usuario, entrada_clave, entrada_pregunta, pregunta_seleccionada):
    clave_valida = True
    nombre_valido = True
    nombre_usado = False
    with open("archivo_datos.csv", "r") as archivo:
        datos = leer_archivo_datos(archivo)
    if entrada_usuario.get() in datos.keys():
        nombre_usado = True
        motivo = "Nombre Usado"
    if not validar_clave(entrada_clave.get()):
        clave_valida = False
        motivo = "Clave invalida"
    if not validar_nombre(entrada_usuario.get()):
        nombre_valido = False
        motivo = "Nombre invalido"

    if clave_valida and nombre_valido and not nombre_usado:
        guardar_archivo(entrada_usuario, entrada_clave, entrada_pregunta, pregunta_seleccionada)
        validacion = Label(raiz3, text=f"La validación fue exitosa", name="validacion")
        resultado = True
    else:
        validacion = Label(raiz3, text=f"No se pudo crear la cuenta: {motivo}", name="validacion")
        resultado = False
    validacion.pack(pady=5)
    return resultado

    
def guardar_archivo(entrada_usuario, entrada_clave, entrada_pregunta, pregunta_seleccionada):
    with open("archivo_datos.csv", "a") as archivo_datos:
        archivo_datos.write(f'{entrada_usuario.get()},{entrada_clave.get()},{entrada_pregunta.get()},{pregunta_seleccionada_global},{0}\n')
