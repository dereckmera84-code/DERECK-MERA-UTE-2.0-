import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
 
# ---------- Paleta de colores ----------
COLOR_FONDO_TARJETA = "#0F2E52"   # azul oscuro semitransparente-look
COLOR_ACCENTO = "#2966AC"         # azul principal
COLOR_ACCENTO_HOVER = "#3A7BC8"
COLOR_TEXTO_CLARO = "#EAF1FB"
COLOR_TEXTO_SUAVE = "#9FBFE2"
COLOR_EXITO = "#4CAF50"
COLOR_ERROR = "#E86A6A"
FUENTE_TITULO = ("Segoe UI", 30, "bold")
FUENTE_SUBTITULO = ("Segoe UI", 12)
FUENTE_LABEL = ("Segoe UI", 12)
FUENTE_ENTRY = ("Segoe UI", 12)
FUENTE_BOTON = ("Segoe UI", 12, "bold")
 
 
def validar_cedula(cedula):
    if len(cedula) != 10:
        return False
    if not cedula.isdigit():
        return False
    return True
 
 
class VentanaRegistro(tk.Tk):
    def __init__(self, imagen_path="Santa_Lucia.jpg"):
        super().__init__()
        self.title("Santa Lucía")
        self.geometry("600x800")
        self.resizable(False, False)
        self.configure(bg=COLOR_ACCENTO)
 
        self._configurar_estilos()
 
        self.imagen_tk = None
        try:
            imagen = Image.open(imagen_path).resize((600, 800))
            self.imagen_tk = ImageTk.PhotoImage(imagen)
        except Exception:
            # Si no existe la imagen, seguimos con un fondo de color plano
            pass
 
        self.ventana_opciones = None
        self.crear_widgets()
 
    def _configurar_estilos(self):
        style = ttk.Style(self)
        style.theme_use("clam")
 
        style.configure(
            "Card.TFrame",
            background=COLOR_FONDO_TARJETA,
            borderwidth=0,
        )
        style.configure(
            "Card.TLabel",
            background=COLOR_FONDO_TARJETA,
            foreground=COLOR_TEXTO_CLARO,
            font=FUENTE_LABEL,
        )
        style.configure(
            "Estado.TLabel",
            background=COLOR_FONDO_TARJETA,
            font=("Segoe UI", 11, "bold"),
        )
        style.configure(
            "TEntry",
            fieldbackground="white",
            padding=8,
            font=FUENTE_ENTRY,
        )
        style.configure(
            "Accent.TButton",
            background=COLOR_ACCENTO,
            foreground="white",
            font=FUENTE_BOTON,
            padding=(14, 10),
            borderwidth=0,
        )
        style.map(
            "Accent.TButton",
            background=[("active", COLOR_ACCENTO_HOVER)],
        )
        style.configure(
            "Secondary.TButton",
            background=COLOR_TEXTO_SUAVE,
            foreground=COLOR_FONDO_TARJETA,
            font=("Segoe UI", 11),
            padding=(14, 8),
            borderwidth=0,
        )
        style.map(
            "Secondary.TButton",
            background=[("active", "#c3d8f0")],
        )
 
    def crear_widgets(self):
        # --- Fondo ---
        if self.imagen_tk is not None:
            fondo = tk.Label(self, image=self.imagen_tk)
            fondo.place(x=0, y=0, relwidth=1, relheight=1)
        else:
            fondo = tk.Label(self, bg=COLOR_ACCENTO)
            fondo.place(x=0, y=0, relwidth=1, relheight=1)
 
        # --- Tarjeta central semitransparente-look ---
        tarjeta = ttk.Frame(self, style="Card.TFrame", padding=30)
        tarjeta.place(relx=0.5, rely=0.5, anchor="center", width=440)
 
        ttk.Label(
            tarjeta,
            text="Bienvenido a",
            style="Card.TLabel",
            font=FUENTE_SUBTITULO,
        ).pack()
 
        ttk.Label(
            tarjeta,
            text="Santa Lucía",
            style="Card.TLabel",
            font=FUENTE_TITULO,
            foreground=COLOR_TEXTO_SUAVE,
        ).pack(pady=(0, 20))
 
        ttk.Label(tarjeta, text="Nombre completo", style="Card.TLabel").pack(
            anchor="w", pady=(10, 4)
        )
        self.entrada_nombre = ttk.Entry(tarjeta, font=FUENTE_ENTRY)
        self.entrada_nombre.pack(fill="x", ipady=4)
 
        ttk.Label(tarjeta, text="Cédula de identidad", style="Card.TLabel").pack(
            anchor="w", pady=(16, 4)
        )
        self.entrada_cedula = ttk.Entry(tarjeta, font=FUENTE_ENTRY)
        self.entrada_cedula.pack(fill="x", ipady=4)
        self.entrada_cedula.bind("<Return>", lambda e: self.registrar())
 
        self.estado_registro = ttk.Label(
            tarjeta, text="", style="Estado.TLabel"
        )
        self.estado_registro.pack(pady=(14, 6))
 
        botones = ttk.Frame(tarjeta, style="Card.TFrame")
        botones.pack(fill="x", pady=(16, 0))
 
        ttk.Button(
            botones,
            text="Registrarse",
            style="Accent.TButton",
            command=self.registrar,
        ).pack(fill="x", pady=(0, 10))
 
        ttk.Button(
            botones,
            text="Ir a opciones →",
            style="Secondary.TButton",
            command=self.siguiente_opcion,
        ).pack(fill="x")
 
    def registrar(self):
        nombre = self.entrada_nombre.get().strip()
        cedula = self.entrada_cedula.get().strip()
 
        if not nombre or not cedula:
            self.estado_registro.config(
                text="⚠ Complete todos los campos.", foreground=COLOR_ERROR
            )
            return
 
        if not validar_cedula(cedula):
            self.estado_registro.config(
                text="✗ Cédula inválida.", foreground=COLOR_ERROR
            )
            return
 
        self.estado_registro.config(
            text=f"✓ ¡Registro completo, {nombre}!", foreground=COLOR_EXITO
        )
 
    def siguiente_opcion(self):
        nombre = self.entrada_nombre.get().strip()
        cedula = self.entrada_cedula.get().strip()
 
        if not nombre or not cedula:
            messagebox.showwarning(
                "Datos incompletos",
                "Por favor ingrese su nombre y su cédula antes de continuar.",
            )
            return
 
        if not validar_cedula(cedula):
            messagebox.showerror("Cédula inválida", "La cédula ingresada no es válida.")
            return
 
        self.withdraw()
        if self.ventana_opciones is not None:
            self.ventana_opciones.deiconify()
 
