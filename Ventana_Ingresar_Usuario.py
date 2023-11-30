from tkinter import *
from Ventana_Cifrados import crear_ventana_cifrados
from Ventana_Recuperacion import crear_ventana_recuperacion
from Funciones_Cifrados import leer_archivo_datos

def ingreso_usuario(raiz_vieja):
    raiz_vieja.destroy()
    global raiz_ingreso
    raiz_ingreso = Tk()
    raiz_ingreso.title("Identificación para acceso")
    raiz_ingreso.geometry("700x450")
    raiz_ingreso.resizable(0,0)
    raiz_ingreso.iconbitmap("icono.ico")

    label_ingreso_usuario = Label(raiz_ingreso , text="Ingrese su usuario")
    label_ingreso_usuario.config(padx=10 , pady=10 , font=("Arial" , 12))

    entry_ingreso_usuario = Entry(raiz_ingreso)
    entry_ingreso_usuario.config(bg="pink")
    entry_ingreso_usuario.place(width=200 , height=40)

    label_ingreso_clave = Label(raiz_ingreso , text="Ingrese su clave")
    label_ingreso_clave.config(padx=10 , pady=10 , font=("Arial" , 12))

    entry_ingreso_clave = Entry(raiz_ingreso)
    entry_ingreso_clave.config(bg="pink")
    entry_ingreso_clave.place(width=200 , height=40)

    iniciar_sesion = Button(raiz_ingreso, text="INICIAR SESIÓN", command=lambda: verificar_cuenta(entry_ingreso_usuario,entry_ingreso_clave))
    iniciar_sesion.config(bg="green" , width=25 , height=2)

    recuperacion_clave = Button(raiz_ingreso, text="Recuperar clave", command=lambda: crear_ventana_recuperacion(raiz_ingreso))
    recuperacion_clave.config(bg="red")

    label_ingreso_usuario.pack(pady=10)
    entry_ingreso_usuario.pack(pady=10)
    label_ingreso_clave.pack(pady=10)
    entry_ingreso_clave.pack(pady=10)
    iniciar_sesion.pack(pady=20)
    recuperacion_clave.pack(pady=20)
    raiz_ingreso.mainloop()

def verificar_cuenta(entrada_usuario,entrada_clave):
    usuario = entrada_usuario.get()
    clave = entrada_clave.get()
    with open("archivo_datos.csv", "r") as archivo:
        datos = leer_archivo_datos(archivo)
    if not usuario in datos.keys():
        resultado = False
        motivo = "Usuario no registrado"
    elif not datos[usuario][1] == clave:
        resultado = False
        motivo = "El nombre y la contraseña no coinciden"
    else:
        resultado = True
    if resultado:
        crear_ventana_cifrados(raiz_ingreso, usuario)
    else:
        validacion = Label(raiz_ingreso,text=motivo, name="verificar_cuenta")
        validacion.pack(pady=5)
    return resultado
