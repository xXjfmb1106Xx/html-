import tkinter as tk 

ventana = tk.Tk()
ventana.Title("Calculadora de articulos")
ventana.Geometry("300x200")

titulo = tk.Label(ventana, text="Calculadora de articulos")
titulo.pack()
decoracion = tk.Label(ventana, text="Ingrese precio: ")
decoracion = decoracion.Entry(ventana)
decoracion.pack()
resultado = tk.Label(ventana, text="total: ")
resultado.pack()
boton = tk.Button(ventana, text="Calcular", command=calcular)
boton.pack()
def calcular():
    precio = [decoracion.get()]
    for a  in precio:
        a = [decoracion.get()]
        if precio == "" or not precio.isdigit():
            total = 0
        resultado = []
        resultado.append(total)
        resultado.config(text=f"total: {total}")
    resultado.pack()