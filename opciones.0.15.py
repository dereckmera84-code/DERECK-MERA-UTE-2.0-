import tkinter as tk
from tkinter import ttk, messagebox

import tema
import datos
from herramientas import(ventanaStock,
ventanaProveedores,ventanaCompras,
ventanaVentas)

class ventanaOpciones(tk.Toplevel):
 def __init__(self, parent):
  super().__init__(parent)
  self.parent= parent
  self.title("Santa Lucia - Opciones")
  self.geometry("800x800")
  self.resizable(False, False)
  self.configure(bg=tema)
  self.withdraw()

  style= ttk.Style(self)
  tema.aplicar_tema(style)

  self.ventanas_herramientas= {}
  self.crear_widget()

def crear_widget(self):
 contenedor= ttk.Frame(self,
 style="Fondo.TFrame",
 padding=42)
 contenedor.pack(fill="both",
 expand=True)

 ttk.Label(contenedor,
 text="Opciones",
 style="Titulo.TLabel").pack(pady=(0, 30))

 ttk.Label(contenedor,
 text="Selecicione Su preferencia",
 style="Texto.TLabel").pack(anchor="w", pady=(22, 10))

 marco_radio= ttk.Frame(contenedor,
 style="Fondo.TFrame")
 marco_radio.pack(fill="x", pady=(0, 22))

 self.herramientas_var =tk.StringVar(value="ninguno")
 for texto, valor in [
 ("Stock", "Stock"),
 ("Proveedor","Proveedor"),
 ("Compras","Compras"),
 ("Ventas","Ventas")
 ]:
  ttk.Radiobutton(marco_radio,
 text=texto, variable=self.herramientas_var,
 value=valor).pack(anchor="w", pady=4)
 
 ttk.Label(contenedor,
 text="Desplegar-ventana ",
 style="Accent.TButton",
 command=self.Desplegar_ventana).pack(anchor="w", pady=(16, 0))

 ttk.Button(contenedor,
 text="volver",
 style="Secondary.TButton",
 command=self.volver_inicio).pack(anchor="w", pady=(40, 0))

def abrir_herramienta(self):
 seleccion=self.herramientas_var.get()
 if seleccion == "ninguno":
  messagebox.showwarning("Sin selección",
 "Seleccione unas ventana antes de continuar.")
  return
 if seleccion in self.ventanas_herramientas:
  self.ventanas_herramientas[seleccion].deiconify()
  self.ventanas_herramientas[seleccion].lift()
  return

 mapa_herramientas= {
  "Stock":(ventanaStock, datos.stock),
  "Proveedor":(ventanaProveedores, datos.proveedores),
  "Compras":(ventanaCompras, datos.compras),
  "Ventas":(ventanaVentas, datos.ventas)}

 Claseventana, lista_datos= mapa_herramientas
 ventana= Claseventana(self, lista_datos)
 self.ventana_herramientas[seleccion]= ventana
 ventana.deiconify()

def volver_inicio(self):
 self.withdraw()
 self.parent.deiconify()
