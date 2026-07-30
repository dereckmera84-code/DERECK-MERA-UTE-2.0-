import tkinter as tk
from registro import validar_cedula

class VentanaOpciones(tk.Toplevel):
 def __init__(self, parent):
  super().__init__(parent)
  self.parent = parent
  self.title("Santa Lucia - Opciones")
  self.geometry("600x800")
  self.resizable(False, False)
 
 
  self.herramientas_var = tk.StringVar(value="ninguno")
  self.protocol("Wm_delete_whindow", self.volver_inicio)
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
 
  self.frame_detalle = tk.Frame(self, bd=2, relief=tk.GROOVE)
  self.frame_detalle.pack(fill=tk.BOTH, padx=20, pady=10)
 
  self.label_detalle = tk.Label(self.frame_detalle, text="", justify="left", wraplength=500)
  self.label_detalle.pack(padx=10, pady=10)
 
  self.lista_stock = tk.Listbox(self.frame_detalle, height=8, width=40)
  self.lista_stock.pack(padx=10, pady=10)
  self.lista_stock.pack_forget()
 
  self.herramientas_var.trace_add("write", lambda *args: self.actualizar_detalle())
  self.actualizar_detalle()
 
  tk.Button(self,
  text="Volver",
  command=self.volver_inicio
  ).pack(pady=20)
 
 def actualizar_detalle(self, *args):
  opcion = self.herramientas_var.get()
 
  if opcion == "Stock":
   self.label_detalle.config(text="Lista de stock disponible:")
   self.lista_stock.delete(0, tk.END)
   stock = [
   "Valvulas - 40 unidades",
   "Llave inglesa - 30 unidades",
   "Pernos - 200 unidades",
   "Brocas - 30 unidades",
   "Taladros - 25 unidades",
   "Cemento de contacto - 70 unidades",
   "Silicona - 40 unidades",
   "Flexometro -50 unidades",
   "Enchufes - 100 unidades",
   "Destornilladores 30 unidades"
   ]
   for item in stock:
    self.lista_stock.insert(tk.END, item)
   self.lista_stock.pack(padx=10, pady=10)
  elif opcion == "Proveedor":
   self.label_detalle.config(text="Lista de proveedores:")
   self.lista_stock.delete(0, tk.END)
   proveedores = [
    "Grupo DIH_Telefono: 0987654321",
    "Fehierro_Telefono: 0981670800",
    "Imporferri_Telefono: 099599651",
    "OTECE_Telefono: 0981756302",
    "Hansa_Telefono: 0995240411",
    "Importrade_Telefono: 0991857904",
    "InporTVEZ_Telefono: 0998044772",
    "Veracruz_Telefono: 098573631",
    "Herpro_Telefono: 098847725"
   ]
   for item in proveedores:
    self.lista_stock.insert(tk.END, item)
   self.lista_stock.pack(padx=10, pady=10)
  elif opcion == "Compras":
   self.label_detalle.config(text="Historal de compras:")
   self.lista_stock.delete(0, tk.END)
   compras = [

   ]
   for item in compras:
    self.lista_stock.insert(tk.END, item)
   self.lista_stock.pack(padx=10, pady=10)
  elif opcion == "Ventas":
   self.label_detalle.config(text="Historial de ventas:")
   self.lista_stock.delete(0, tk.END)
   ventas = [
   
    
   ]
   for item in ventas:
    self.lista_stock.insert(tk.END, item)
   self.lista_stock.pack(padx=10, pady=10)
  else:
   self.lista_stock.pack_forget()
   mensaje = "Seleccione una opción para ver información."
   self.label_detalle.config(text=mensaje)

 def volver_inicio(self):
  self.withdraw()
  self.parent.deiconify()

