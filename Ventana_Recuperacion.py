from tkinter import *
from Funciones_Cifrados import leer_archivo_datos

def crear_ventana_recuperacion(raiz_ingreso):
    raiz_ingreso.destroy()
    global raiz_recuperacion
    raiz_recuperacion = Tk()
    raiz_recuperacion.title("Recuperacion Clave")
    raiz_recuperacion.geometry("700x450")
    raiz_recuperacion.resizable(0,0)
    raiz_recuperacion.iconbitmap("icono.ico")

    label_recuperacion_usuario = Label(raiz_recuperacion , text="Ingrese su usuario")
    label_recuperacion_usuario.config(padx=10 , pady=10 , font=("Arial" , 12))

    entrada_recuperacion_usuario = Entry(raiz_recuperacion)
    entrada_recuperacion_usuario.config(bg="pink")
    entrada_recuperacion_usuario.place(width=200 , height=40)

    recuperacion_cuenta = Button(raiz_recuperacion , text="RECUPERAR CUENTA" , command =lambda:verificar_usuario(entrada_recuperacion_usuario))
    recuperacion_cuenta.config(bg="red" , width=25 , height=2)

    label_recuperacion_usuario.pack(pady=10)
    entrada_recuperacion_usuario.pack(pady=10)
    recuperacion_cuenta.pack(pady=20)
    raiz_recuperacion.mainloop()

def verificar_usuario(entrada_recuperacion_usuario):
    usuario = entrada_recuperacion_usuario.get()
    with open("archivo_datos.csv","r") as archivo:
        datos = leer_archivo_datos(archivo)

    if usuario not in datos.keys():
        resultado = False
        motivo = "La cuenta con ese nombre no existe"
    else:
        resultado = True
    pregunta_seleccionada = Label(raiz_recuperacion , text=f"Pregunta: {datos[usuario][3]}" , name="pregunta_recuperacion")
    pregunta_seleccionada.pack(pady=10)

    entrada_respuesta = Entry(raiz_recuperacion , name="respuesta_recuperacion")
    entrada_respuesta.config(bg="pink")
    entrada_respuesta.pack(pady=10)
    
    boton_respuesta = Button(raiz_recuperacion , text="Verificar respuesta", name="boton_respuesta", command=lambda: verificar_respuesta(entrada_respuesta, usuario))
    boton_respuesta.config(bg="red")
    boton_respuesta.pack(pady=10)
    return resultado

def verificar_respuesta(entrada_respuesta, usuario):
    with open("archivo_datos.csv","r") as archivo:
        datos = leer_archivo_datos(archivo)
    if datos[usuario][2] != entrada_respuesta.get():
        resultado = False
        motivo = "Respuesta Incorrecta"
    else:
        resultado = True
        motivo = (f"Su Clave es{datos[usuario][1]}")
            
    devolver_clave = Label(raiz_recuperacion, text=motivo, name="devolver_clave")
    devolver_clave.pack(pady=10)
    return resultado
