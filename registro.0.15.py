import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

#PALETA DE COLORES:
COLOR_FONDO= "#0F2E52"
COLOR_ACCENTO= "#2966AC"
COLOR_ACCENTO_HOVER= "#3A7BC8"
COLOR_TEXTO_CL= "#EAF1FB"
COLOR_TEXTO_SB="#9FBFE2"
COLOR_EXITO= "#4CAF50"
COLOR_ERROR= "#E86A6A"

#FUENTES DE LETRAS:
FUENTE_TITULO=("Segoe UI, 30", "bold")
FUENTE_SUBTITULO=("Segoe UI, 12")
FUENTE_LABEL=("Segoe UI, 12")
FUENTE_ENTRY=("Segoe UI, 12")
FUENTE_BOTON=("Segoe UI, 12", "bold")

def validar_cedula(cedula):
 if len(cedula) !=10:
  return False
 if not cedula.isdigit():
  return False
 return True

class VentanaRegistro(tk.Tk):
 def __init__(self, imagen_path="Santa_Lucia.jpg"):
  super().__init__()
  self.title("Santa Lucia")
  self.geometry("600x800")
  self.resizable(False, False)
  self.configure(bg=COLOR_ACCENTO)

  self.configurar_estilos()

  self.imagen_tk= None
  try:
    imagen=Image.open(imagen.path).rezise((600, 800))
    self.imagen_tk=self.imageTk.photoimage(imagen)
  except Exception:
   pass
  self.ventana_opciones=None
  self.crear_widget()

def configurar_estilo(self):
 style= ttk.Style(self)
 style.theme_use("clam")

 style.configure("Card.TFrame",
 background=COLOR_FONDO,
 borderwidth=0)

 style.configure("Card TLabel",
 background=COLOR_FONDO,
 foreground=COLOR_TEXTO_CL,
 font=FUENTE_LABEL)

 style.configure("Estado TLabel",
 background=COLOR_FONDO,
 font=("Segoe UI", 11, "bold"))

 style.configure("TEntry",
 fieldbacjground="#F7F8FA",
 padding=8, font=FUENTE_ENTRY)

 style.configure("Accent.TButton",
 backgroound=COLOR_ACCENTO,
 foreground="#F7F8FA",
 font=FUENTE_BOTON,
 padding=(14,10),
 borderwidth=0)

 style.map("Accent.TButton",
 background=[("active", COLOR_ACCENTO_HOVER)])

 style.configure("Secondary.TButton",
 background=COLOR_TEXTO_SB,
 foreground=COLOR_FONDO,
 font=("Segoe UI", 11), padding=(14,18),
 borderwidth=0)

 style.map("Secondary.TButton",
 background=[("active", "#C3D8F0")])

def crear_widget(self):
 if self.imagen_tk is not None:
  fondo = tk.Label(self, image=self.imagen_tk)
  fondo.place(x=0, y=0, relwidth=1, relheight=1)
 else:
   fondo = tk.Label(self, bg=COLOR_ACCENTO)
 fondo.place(x=0, y=0, relwidth=1, relheight=1)

 tarjeta = ttk.Frame(self, style="Card.TFrame", padding=30)
 tarjeta.place(relx=0.5, rely=0.5, anchor="center", width=440)
 
 ttk.Label(tarjeta,
 text="Bienvenido a",
 style="Card.TLabel",
 font=FUENTE_SUBTITULO).pack()

 ttk.Label(tarjeta,
 text="Santa Lucía",
 style="Card.TLabel",
 font=FUENTE_TITULO,
 foreground=COLOR_TEXTO_SB).pack(pady=(0, 20))

 ttk.Label(tarjeta,
 text="Nombre completo",
 style="Card.TLabel").pack(
 anchor="w", pady=(10, 4))

 self.entrada_nombre = ttk.Entry(tarjeta,
 font=FUENTE_ENTRY)
 self.entrada_nombre.pack(fill="x", ipady=4)

 ttk.Label(tarjeta,
 text="Cédula de identidad",
 style="Card.TLabel").pack(
 anchor="w", pady=(16, 4))

 self.entrada_cedula=ttk.Entry(tarjeta,
 font=FUENTE_ENTRY)
 self.entrada_cedula.pack(fill="x", ipady=4)

 self.entrada_cedula.bind("<Return>",
 lambda e: self.registrar()) 

 self.estado_registro=ttk.Label(tarjeta,
 text="", style="Estado TLabel")

 self.estado_registro.pack(pady=(14, 6))

 botones = ttk.Frame(tarjeta,
 style="Card.TFrame")
 botones.pack(fill="x", pady=(16, 0))

 ttk.Button(botones,
 text="Registrarse",
 style="Accent.TButton",
 command=self.registrar,
 ).pack(fill="x", pady=(0, 10))

 ttk.Button(botones,
 text="Ir a opciones →",
 style="Secondary.TButton",
 command=self.siguiente_opcion,
 ).pack(fill="x")

def registrar(self):
 nombre = self.entrada_nombre.get().strip()
 cedula = self.entrada_cedula.get().strip()
 
 if not nombre or not cedula:
  self.estado_registro.config(text=" Complete todos los campos.",
  foreground=COLOR_ERROR )
  return 

 if not validar_cedula(cedula):
  self.estado_registro.config(text=" Cédula inválida.",
  foreground=COLOR_ERROR)
  return

 self.estado_registro.config(text=f"¡Registro completo, {nombre}!",
 foreground=COLOR_EXITO)

def siguiente_opcion(self):
 nombre = self.entrada_nombre.get().strip()
 cedula = self.entrada_cedula.get().strip()

 if not nombre or not cedula:
   messagebox.showwarning("Datos incompletos",
   "Por favor ingrese su nombre y su cédula antes de continuar.")
   return
 
 if not validar_cedula(cedula):
  messagebox.showerror("Cédula inválida",
  "La cédula ingresada no es válida.")
  return
 
 self.withdraw()
 if self.ventana_opciones is not None:
  self.ventana_opciones.deiconify()
  
 
        self.withdraw()
        if self.ventana_opciones is not None:
            self.ventana_opciones.deiconify()
 
