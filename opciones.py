import tkinter as tk
from registro import validar_cedula

class VentanaOpciones(tk.Toplevel):
 def __init__(self, parent):
  super().__init__(parent)
  self.parent = parent
  self.title("Santa Lucia - Opciones")
  self.geometry("600x800")
  self.withdraw()
 
  self.crear_widgets()
 
 def crear_widgets(self):
  self.opcion = tk.IntVar()
  tk.Checkbutton(
  self,
  text="Recordar mis preferencias",
  variable=self.opcion,
  font=("Arial", 14)
 ).pack(pady=10)
 
  self.herramientas_var = tk.StringVar(value="ninguno")
 
  tk.Label(self, text="Seleccione su preferencia"
 ).pack()
 
  for texto, valor in [
 ("Stock", "Stock"),
 ("Proveedor", "Proveedor"),
 ("Compras", "Compras"),
 ("Ventas", "Ventas"),
 ]:
   tk.Radiobutton(
  self,
  text=texto,
  variable=self.herramientas_var,
  value=valor
 ).pack()
 
  tk.Label(self,
  text="Seleccion de herramientas:"
  ).pack(pady=10)
 
  tk.Button(self,
  text="Volver",
  command=self.volver_inicio
  ).pack(pady=20)
 
 def volver_inicio(self):
  self.withdraw()
  self.parent.deiconify()


