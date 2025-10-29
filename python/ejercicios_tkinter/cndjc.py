import tkinter as tk 
ventana = tk.Tk()
ventana.title("lista de productos")
ventana.geometry("400x400")
lista = tk.Listbox(ventana,width = 50)

productos = (("arroz",2400,30),("arroz",2400,30),("arroz",2400,30),("arroz",2400,30),("arroz",2400,30),)

for item in productos :
    cosa = f"producto: {item[0]}, precio{item[1]}, cantidad: {item[2]}"
    lista.insert(tk.END, cosa)
def mostrar_productos():
    lista.grid(row=1,column=0,columnspan=4)
    boton.config(text="ocultar productos", command=ocultar_productos)
def ocultar_productos():
    lista.grid_forget()
    boton.config(text = "mostrar productos", command=mostrar_productos)
boton=tk.Button(ventana,text="mostrar productos", command= mostrar_productos)
boton.grid(row=0 ,column = 0, sticky = "nwes")
ventana.mainloop()