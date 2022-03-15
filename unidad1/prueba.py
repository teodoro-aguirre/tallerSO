import tkinter as tk  # Importar antes de usar Tkinter

import tkinter.messagebox

import pickle

 

# Paso 1, crea una instancia del objeto y crea una ventana

window = tk.Tk()

 

# Paso 2, nombre la visualización de la ventana

window.title('VENTANA PRINCIPAL')

 

# Paso 3, establezca el tamaño de la ventana (largo * ancho)

window.geometry('400x300')  # Aquí la multiplicación es pequeña x

 

# Paso 5, información del usuario

tk.Label(window, text='HOLAAAA', font=('Arial', 14)).place(x=10, y=170)
 


ventana_grabar = tk.Toplevel(window)

ventana_grabar.geometry('300x200')

ventana_grabar.title('Grabar')
 


window.mainloop()