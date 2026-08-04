import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
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
  self.geometry("800x800")
  self.resizable(False, False)
  self.configure(bg="#2966AC")

  self._configurar_estilo()
  self.imagen_tk = None
  
  imagen = Image.open(imagen_path)
  self.imagen_tk = ImageTk.PhotoImage(imagen)
  except Exception:

  pass

  self.ventana_opciones = None
  self.crear_widgets()

def _configurar_estilo(self):
  style = tk.ttk.Style()
  style.claim("clam")


  style.configure("Card.label",
  background="#2966AC",
  borderwidth=0,
  )

  style.configure("card.label",
  background="#071D36",
  borderwidth=0,
  font=("Arial", 16)
  )

  style.configure("Card.label",
  background="#9FBFE2",
  font=("Arial",16)
  )

  style.configure("Card.label",
  "entry",
  fieldbackground="#E5EAF0")
  padding = 10
  font = "#E5EAF0"

  style.configure("Accent.TButton",
  background="#2966AC",
  foreground="#E5EAF0",
  font="#071D36",
  padding=(14, 10),
  borderwidth=0,
  )
  style.map(
  "Accent.tButton",
  background=[("active", "#9FBFE2")],  
  )

  style.configure("Secundary.TButton",
  background="#9FBFE2",
  foreground="#2966AC",
  font="#071D36",
  padding=(14, 10),
  borderwidth=0,
  )
  style.map(
  "Secundary.TButton",
  background=[("active", "#2966AC")],
  foreground=[("active", "#E5EAF0")]
  )

def _crear_widgets(self):
 if self.imagen_tk:
  fondo = tk.Label(self,
  image=self.imagen_tk)
  fondo.place(x=0,
  y=0, relwidth=1,
  relheight=1)  
 else:
  fondo = tk.Label(self,
  bg="#2966AC")
  fondo.place(x=0,
  y=0, relwidth=1,
  relheight=1)
  
  tarjeta = tk.Frame(self,
  bg="#071D36",
  bd=2, relief=tk.GROOVE)
  tarjeta.place(relx=0.5,
  rely=0.5, anchor="center",
  width=400, height=400)

 ttk.Label(tarjeta,
 text="Bienvenido a",
 style="Card.label",
 font="#5C81AA",
 ).pack()
 ttk.Label(tarjeta,
 text="Santa Lucía",
 style="Card.TLabel",
 font="#071D36",
 foreground="#5C81AA",
 ).pack(pady=(0, 20))

 ttk.Label(tarjeta,
 text="Ingrese su nombre:",
 style="Card.Tlabel",
 ).pack(anchor= "w", pady=(10, 5)
 )

 self.entrada_cedula = ttk.Entry(tarjeta,
 font="#071D36",)
 self.entrada_cedula.pack(fill="x",
 ipady=5)
 self.entrada_cedula.bind("<return>",
 lambda e: self.registrar())

 self.estado_registro= ttk.label(tarjeta,
 text="", style="Estado.Tlabel"
 )
 self.estado_registro.pack(pady=(15, 6))

 botones = ttk.Frame(tarjeta, style="Card.TFrame")
 botones.pack(fill="x", pady=(15,0))
 ttk.Button(botones,
 text="Registrarse",
 style="Accent.TButton",
 command=self.siguente_opcion,
 ).pack(fill="x")

def registrar(self):
 nombre = self.entrada_nombre.get().strip()
 cedula = self.emtrada_cedula.get().strip()
 if not nombre or not cedula:
  self.estado_registrado.config(
  text="Por favor, complete todos los campos.",
  foreground="#C01F1F"
  )
  return
 if not validar_cedula(cedula):
  self.estado_registrado.config(
  text="Cedula invalida.",
  foreground="#C01F1F"
 )
  return
 self.estado_registro.config(
 text=f"Registro Completado., {nombre}!",
 foreground="#3BCE3B",
 )

def siguente_opcion(self):
  nombre = self.entrada_nombre.get().strip()
  cedula = self.entrada_cedula.get().strip()

  if not nombre or not cedula:
   messagebox.showerror("Datos incompletos",
  "Por favor, ingrese su nombre y cédula antes de continuar.")
  return

if not validar_cedula(cedula):
  messagebox.showerror("Cedula invalida",
 "la cedula ingresada no es valida.")
  
  return

  self.withdraw()
  if self.ventana_opciones:
   self.ventana_opciones.deiconify()
   
