import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


def siguiente_opcion():
 nombre = entrada_nombre.get().strip()
 cedula = entrada_cedula.get().strip()

 if not nombre or not cedula:
  messagebox.showwarning(
 "Datos incompletos",
 "Por favor ingrese su nombre y su cédula antes de continuar."
 )
  return

 ventana1.withdraw()
 ventana2.deiconify()


def volver_inicio():
 ventana2.withdraw()
 ventana1.deiconify()


def registrar():
 nombre = entrada_nombre.get().strip()
 cedula = entrada_cedula.get().strip()

 if not nombre or not cedula:
     estado_registro.config(text="Complete todos los campos.", 
    fg="red")
     return

 estado_registro.config(
 text=f"¡Registro completo, {nombre}!",
 fg="green"
)


ventana1 = tk.Tk()
ventana1.title("Santa Lucia")
ventana1.geometry("600x800")

imagen = Image.open("santa_lucia.jpg")
imagen = imagen.resize((600,800))
imagen_tk = ImageTk.PhotoImage(imagen)

fondo = tk.Label( ventana1, image=imagen_tk )
fondo.place(x = 0 , y = 0 , relwidth=1, relheight=1)

texto = tk.Label(
 ventana1,
 text="Bienvenido a Santa Lucia",
 font=("Arial",36,"bold"), 
 fg="#9FBFE2",
 bg="#2966AC"    
)
texto.place(relx=0.5 ,rely=0.5, anchor="center")



tk.Label(
 ventana1,
 text="Ingrese su nombre:",
 font=("Arial", 16)
).pack(pady=10)

entrada_nombre = tk.Entry(
 ventana1,
 fg="#071D36",
 font=("Arial", 16)
)
entrada_nombre.pack(pady=10)

tk.Label(
 ventana1,
 text="Ingrese su cedula de identidad:",
 font=("Arial", 16)
).pack(pady=10)

entrada_cedula = tk.Entry(
 ventana1,
 fg="#062344",
 font=("Arial", 16)
)
entrada_cedula.pack(pady=10)

estado_registro = tk.Label(
 ventana1,
 text="",
 font=("Arial", 12)
)
estado_registro.pack(pady=5)

tk.Button(
 ventana1,
 text="Registro",
 command=registrar
).pack(pady=10)

tk.Button(
 ventana1,
 text="Ir al apartado de opciones",
 command=siguiente_opcion
).pack(pady=10)

ventana2 = tk.Toplevel(ventana1)
ventana2.title("Santa Lucia - Opciones")
ventana2.geometry("500x400")
ventana2.withdraw()

opcion = tk.IntVar()

tk.Checkbutton(
 ventana2,
 text="Recordar mis preferencias",
 variable=opcion,
 font=("Arial", 14)
).pack(pady=10)

herramientas_var = tk.StringVar(value="ninguno")

tk.Label(
 ventana2,
 text="Seleccione su preferencia"
).pack()

for texto, valor in [
 ("Stock", "Stock"),
 ("Proveedor", "Proveedor"),
 ("Compras", "Compras"),
 ("Ventas", "Ventas"),
]:
 tk.Radiobutton(
 ventana2,
 text=texto,
 variable=herramientas_var,
 value=valor
 ).pack()

tk.Label(
 ventana2,
 text="Seleccion de herramientas:"
).pack(pady=10)


tk.Button(
 ventana2,
 text="Volver",
 command=volver_inicio
).pack(pady=20)

ventana1.mainloop()
