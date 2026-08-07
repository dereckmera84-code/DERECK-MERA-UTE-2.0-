

        self.crear_widgets(titulo)
        self.cargar_datos_existentes()

    def crear_widgets(self, titulo):
        contenedor = ttk.Frame(self, style="Fondo.TFrame", padding=30)
        contenedor.pack(fill="both", expand=True)

        ttk.Label(contenedor, text=titulo, style="Titulo.TLabel").pack(
            anchor="w", pady=(0, 20)
        )

        # --- Formulario ---
        formulario = ttk.Frame(contenedor, style="Fondo.TFrame")
        formulario.pack(fill="x", pady=(0, 10))

        for i, campo in enumerate(self.campos):
            ttk.Label(formulario, text=campo, style="Texto.TLabel").grid(
                row=0, column=i, sticky="w", padx=(0, 10)
            )
            entrada = ttk.Entry(formulario, font=tema.FUENTE_ENTRY, width=14)
            entrada.grid(row=1, column=i, sticky="we", padx=(0, 10))
            entrada.bind("<Return>", lambda e: self.agregar())
            self.entradas[campo] = entrada

        self.estado = ttk.Label(contenedor, text="", style="Estado.TLabel")
        self.estado.pack(anchor="w", pady=(10, 4))

        botones = ttk.Frame(contenedor, style="Fondo.TFrame")
        botones.pack(fill="x", pady=(0, 20))

        ttk.Button(
            botones, text="Agregar", style="Accent.TButton", command=self.agregar
        ).pack(side="left")

        ttk.Button(
            botones, text="← Volver", style="Secondary.TButton", command=self.volver
        ).pack(side="left", padx=(10, 0))

        # --- Tabla ---
        self.tree = ttk.Treeview(
            contenedor, columns=self.campos, show="headings", height=14
        )
        for campo in self.campos:
            self.tree.heading(campo, text=campo)
            self.tree.column(campo, anchor="center", width=100)
        self.tree.pack(fill="both", expand=True)

    def cargar_datos_existentes(self):
        """Si la ventana se vuelve a abrir, repuebla la tabla con lo ya agregado."""
        for registro in self.lista_datos:
            self.tree.insert("", "end", values=[registro[c] for c in self.campos])

    def agregar(self):
        valores = {c: self.entradas[c].get().strip() for c in self.campos}

        if any(v == "" for v in valores.values()):
            self.estado.config(
                text="⚠ Complete todos los campos.", foreground=tema.COLOR_ERROR
            )
            return

        self.lista_datos.append(valores)
        self.tree.insert("", "end", values=[valores[c] for c in self.campos])

        for entrada in self.entradas.values():
            entrada.delete(0, tk.END)

        self.estado.config(text="✓ Registro agregado.", foreground=tema.COLOR_EXITO)

    def volver(self):
        self.withdraw()


class VentanaStock(VentanaHerramienta):
    def __init__(self, parent, lista_datos):
        super().__init__(
            parent,
            titulo="Stock",
            campos=["Producto", "Cantidad", "Precio unitario"],
            lista_datos=lista_datos,
        )


class VentanaProveedores(VentanaHerramienta):
    def __init__(self, parent, lista_datos):
        super().__init__(
            parent,
            titulo="Proveedores",
            campos=["Nombre", "Contacto", "Producto que provee"],
            lista_datos=lista_datos,
        )


class VentanaCompras(VentanaHerramienta):
    def __init__(self, parent, lista_datos):
        super().__init__(
            parent,
            titulo="Compras",
            campos=["Producto", "Cantidad", "Proveedor", "Fecha"],
            lista_datos=lista_datos,
        )


class VentanaVentas(VentanaHerramienta):
    def __init__(self, parent, lista_datos):
        super().__init__(
            parent,
            titulo="Ventas",
            campos=["Producto", "Cantidad", "Cliente", "Fecha"],
            lista_datos=lista_datos,
        )
