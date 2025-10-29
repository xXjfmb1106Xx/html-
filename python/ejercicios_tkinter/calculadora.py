import tkinter as tk 

def click_button(numero):
    actual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, actual + str(numero))
    
def borrar():
    entrada.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")
        
ventana = tk.Tk()
ventana.title("Calculadora con Tkinter")
ventana.geometry("300x400")

entrada = tk.Entry(ventana, width=20, font=("Arial", 24),
justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

botones = [
    ('7'1,0), ('8'1,1), ('9'1,2), ('/'1,3),
    ('4'2,0), ('5'2,1), ('6'2,2), ('*'2,3),
    ('1'3,0), ('2'3,1), ('3'3,2), ('-'3,3),
    ('0'4,0), ('.'4,1), ('='4,2), ('+'4,3),
    ('C'5,0)

ventana.mainloop()
]