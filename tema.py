# --- Constantes que usa herramientas.py directamente ---
COLOR_FONDO = "#0F2E52"
COLOR_ERROR = "#E86A6A"
COLOR_EXITO = "#4CAF50"
FUENTE_ENTRY = ("Segoe UI", 12)


def aplicar_tema(style):

    style.theme_use("clam")
    style.configure("Fondo.TFrame", background="#0F2E52")
    style.configure("Titulo.TLabel",
    background="#0F2E52",
    foreground="#9FBFE2",
    font=("Segoe UI", 12))

    style.configure("Texto.TLabel",
    background="#0F2E52",
    foreground="#EAF1FB",
    font=("Segoe UI", 12))

    style.configure("Estado.TLabel",
    background="#0F2E52",
    font=("Segoe UI", 11, "bold"))

    style.configure("TEntry",
    fieldbackground="#FAFBFD",
    padding=6,
    font=("Segoe UI", 12))
    style.configure("TCheckbutton",
    background="#0F2E52",
    foreground="#EAF1FB",
    font=("Segoe UI", 12))

    style.map("TCheckbutton",
    background=[("active", "#0F2E52")])

    style.configure("TRadiobutton",
    background="#0F2E52",
    foreground="#FAFBFD",
    font=("Segoe UI", 12))

    style.map("TRadiobutton",
    background=[("active", "#2966AC")])

    style.configure("Accent.TButton",
    background="#466991",
    foreground="#FAFBFD",
    font=("Segoe UI", 12, "bold"),
    padding=(14, 8),
    borderwidth=0)

    style.map("Accent.TButton",
    background=[("active", "#3A7BC8")])

    style.configure("Secondary.TButton",
    background="#9FBFE2",
    foreground="#0F2E52",
    font=("Segoe UI", 11),
    padding=(14, 8),
    borderwidth=0)

    style.map("Secondary.TButton",
    background=[("active", "#C3D8F0")])

    style.configure("Treeview",
    background="#FAFBFD",
    fieldbackground="#FAFBFD",
    foreground="#1A1A1A",
    rowheight=25,
    font=("Segoe UI", 10))

    style.map("Treeview.Heading",
    background=[("active", "#3A7BC8")])

    style.configure("Treeview.Heading",
    background="#2966AC",
    foreground="#FAFBFD",
    font=("Segoe UI", 11, "bold"))
