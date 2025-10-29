import tkinter as tk

arroz = ["arroz", 100, 50] 
banano = ["banano", 50, 100] 
naranja =["naranja", 80, 75]

productos = {
    arroz[0]: (arroz[1], arroz[2]),
    banano[0]: (banano[1], banano[2]),
    naranja[0]: (naranja[1], naranja[2])
}
ventana = tk.Tk()

ventana.title("visualizador de productos")
ventana.geometry("500x400")
nombre = tk.Entry(text="nombre del producto")
def boton():
    print("Los productos disponibles son:")
    for productos,precio,cantidad in arroz.items():
        producto = tk.Label(ventana, text=f"{productos}: {precio} pesos cantidad: {cantidad} ")
        print(f"{arroz[0]}: {arroz[1]} pesos cantidad: {arroz[2]} ")
    boton.pack()

ventana.mainloop()