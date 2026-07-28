import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


def validar_cedula(cedula):
 if len(cedula) != 10:
     return False
 if not cedula.isdigit():
     return False
 return True


class VentanaRegistro(tk.Tk):
 def __init__(self, imagen_path="santa_lucia.jpg"):
  super().__init__()
  self.title("Santa Lucia")
  self.geometry("600x800")
 
  self.imagen = Image.open(imagen_path)
  self.imagen = self.imagen.resize((600, 800))
  self.imagen_tk = ImageTk.PhotoImage(self.imagen)
 
  
  self.ventana_opciones = None
 
  self.crear_widgets()
 
 def crear_widgets(self):
  fondo = tk.Label(self, image=self.imagen_tk)
  fondo.place(x=0, y=0, relwidth=1, relheight=1)
 
  texto = tk.Label(
  self,
  text="Bienvenido a Santa Lucia",
  font=("Arial", 36, "bold"),
  fg="#9FBFE2",
  bg="#2966AC"
 )
  texto.place(relx=0.5, rely=0.5, anchor="center")
 
  tk.Label(self, text="Ingrese su nombre:",
  font=("Arial", 16)
  ).pack(pady=10)
  self.entrada_nombre = tk.Entry(self,
  fg="#071D36",
  font=("Arial", 16)
  )
  self.entrada_nombre.pack(pady=10)
 
  tk.Label(self, text="Ingrese su cedula de identidad:",
  font=("Arial", 16)).pack(pady=10)
  self.entrada_cedula = tk.Entry(self,
  fg="#062344", font=("Arial", 16)
  )
  self.entrada_cedula.pack(pady=10)
 
  self.estado_registro = tk.Label(self, text="",
  font=("Arial", 12)
  )
  self.estado_registro.pack(pady=5)
 
  tk.Button(self,
  text="Registro",
  command=self.registrar
  ).pack(pady=10)


  tk.Button(self,
  text="Ir al apartado de opciones",
  command=self.siguiente_opcion
 ).pack(pady=10)
 
 def registrar(self):
  nombre = self.entrada_nombre.get().strip()
  cedula = self.entrada_cedula.get().strip()
 
  if not nombre or not cedula:
   self.estado_registro.config(text="Complete todos los campos.",
   fg="red")
   return

  if not validar_cedula(cedula):
   self.estado_registro.config(text="Cédula inválida.",
   fg="red")
   return
 
  self.estado_registro.config(text=f"¡Registro completo, {nombre}!",
   fg="green")
 
 def siguiente_opcion(self):
  nombre = self.entrada_nombre.get().strip()
  cedula = self.entrada_cedula.get().strip()
 
  if not nombre or not cedula:
   messagebox.showwarning(
  "Datos incompletos",
  "Por favor ingrese su nombre y su cédula antes de continuar."
 )
   return

  if not validar_cedula(cedula):
   messagebox.showerror("Cédula inválida",
   "La cédula ingresada no es válida.")
   return
 
  self.withdraw()
  if self.ventana_opciones is not None:
   self.ventana_opciones.deiconify()
