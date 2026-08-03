import tkinter as tk
from tkinter import ttk, messagebox

import tema
import datos
from herramientas import (
    VentanaStock,
    VentanaProveedores,
    VentanaCompras,
    VentanaVentas,
)


class VentanaOpciones(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Santa Lucía - Opciones")
        self.geometry("800x800")
        self.resizable(False, False)
        self.configure(bg=tema.COLOR_FONDO)
        self.withdraw()

        style = ttk.Style(self)
        tema.aplicar_tema(style)

        # Cada herramienta se crea una sola vez y se reutiliza (para no
        # perder los datos que ya se agregaron cuando se vuelve a abrir).
        self.ventanas_herramientas = {}

        self.crear_widgets()

    def crear_widgets(self):
        contenedor = ttk.Frame(self, style="Fondo.TFrame", padding=40)
        contenedor.pack(fill="both", expand=True)

        ttk.Label(contenedor, text="Opciones", style="Titulo.TLabel").pack(
            pady=(0, 30)
        )

        self.opcion = tk.IntVar()
        ttk.Checkbutton(
            contenedor,
            text="Recordar mis preferencias",
            variable=self.opcion,
        ).pack(anchor="w", pady=10)

        ttk.Label(
            contenedor,
            text="Seleccione su preferencia",
            style="Texto.TLabel",
        ).pack(anchor="w", pady=(20, 8))

        marco_radios = ttk.Frame(contenedor, style="Fondo.TFrame")
        marco_radios.pack(fill="x", pady=(0, 20))

        self.herramientas_var = tk.StringVar(value="ninguno")
        for texto, valor in [
            ("Stock", "Stock"),
            ("Proveedor", "Proveedor"),
            ("Compras", "Compras"),
            ("Ventas", "Ventas"),
        ]:
            ttk.Radiobutton(
                marco_radios,
                text=texto,
                variable=self.herramientas_var,
                value=valor,
            ).pack(anchor="w", pady=4)

        ttk.Label(
            contenedor,
            text="Selección de herramientas:",
            style="Texto.TLabel",
        ).pack(anchor="w", pady=(20, 0))

        ttk.Button(
            contenedor,
            text="Abrir herramienta →",
            style="Accent.TButton",
            command=self.abrir_herramienta,
        ).pack(anchor="w", pady=(14, 0))

        ttk.Button(
            contenedor,
            text="← Volver",
            style="Secondary.TButton",
            command=self.volver_inicio,
        ).pack(anchor="w", pady=(40, 0))

    def abrir_herramienta(self):
        seleccion = self.herramientas_var.get()

        if seleccion == "ninguno":
            messagebox.showwarning(
                "Sin selección", "Seleccione una herramienta antes de continuar."
            )
            return

        # Si la ventana de esa herramienta ya existe, solo la mostramos de nuevo.
        if seleccion in self.ventanas_herramientas:
            self.ventanas_herramientas[seleccion].deiconify()
            self.ventanas_herramientas[seleccion].lift()
            return

        mapa_herramientas = {
            "Stock": (VentanaStock, datos.stock),
            "Proveedor": (VentanaProveedores, datos.proveedores),
            "Compras": (VentanaCompras, datos.compras),
            "Ventas": (VentanaVentas, datos.ventas),
        }

        ClaseVentana, lista_datos = mapa_herramientas[seleccion]
        ventana = ClaseVentana(self, lista_datos)
        self.ventanas_herramientas[seleccion] = ventana
        ventana.deiconify()

    def volver_inicio(self):
        self.withdraw()
        self.parent.deiconify()
