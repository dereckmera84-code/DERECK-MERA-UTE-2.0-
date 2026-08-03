COLOR_FONDO = "#0F2E52"
COLOR_ACCENTO = "#2966AC"
COLOR_ACCENTO_HOVER = "#3A7BC8"
COLOR_TEXTO_CLARO = "#EAF1FB"
COLOR_TEXTO_SUAVE = "#9FBFE2"
COLOR_EXITO = "#4CAF50"
COLOR_ERROR = "#E86A6A"

FUENTE_TITULO = ("Segoe UI", 22, "bold")
FUENTE_SUBTITULO = ("Segoe UI", 12)
FUENTE_LABEL = ("Segoe UI", 12)
FUENTE_ENTRY = ("Segoe UI", 12)
FUENTE_BOTON = ("Segoe UI", 12, "bold")


def aplicar_tema(style):
    """Configura un ttk.Style con el tema visual de Santa Lucía."""
    style.theme_use("clam")

    style.configure("Fondo.TFrame", background=COLOR_FONDO)
    style.configure(
        "Titulo.TLabel",
        background=COLOR_FONDO,
        foreground=COLOR_TEXTO_SUAVE,
        font=FUENTE_TITULO,
    )
    style.configure(
        "Texto.TLabel",
        background=COLOR_FONDO,
        foreground=COLOR_TEXTO_CLARO,
        font=FUENTE_LABEL,
    )
    style.configure(
        "Estado.TLabel",
        background=COLOR_FONDO,
        font=("Segoe UI", 11, "bold"),
    )
    style.configure("TEntry", fieldbackground="white", padding=6, font=FUENTE_ENTRY)
    style.configure(
        "TCheckbutton",
        background=COLOR_FONDO,
        foreground=COLOR_TEXTO_CLARO,
        font=FUENTE_LABEL,
    )
    style.map("TCheckbutton", background=[("active", COLOR_FONDO)])
    style.configure(
        "TRadiobutton",
        background=COLOR_FONDO,
        foreground=COLOR_TEXTO_CLARO,
        font=FUENTE_LABEL,
    )
    style.map("TRadiobutton", background=[("active", COLOR_FONDO)])

    style.configure(
        "Accent.TButton",
        background=COLOR_ACCENTO,
        foreground="white",
        font=FUENTE_BOTON,
        padding=(14, 10),
        borderwidth=0,
    )
    style.map("Accent.TButton", background=[("active", COLOR_ACCENTO_HOVER)])

    style.configure(
        "Secondary.TButton",
        background=COLOR_TEXTO_SUAVE,
        foreground=COLOR_FONDO,
        font=("Segoe UI", 11),
        padding=(14, 8),
        borderwidth=0,
    )
    style.map("Secondary.TButton", background=[("active", "#c3d8f0")])

    style.configure(
        "Treeview",
        background="white",
        fieldbackground="white",
        foreground="#1a1a1a",
        rowheight=28,
        font=("Segoe UI", 10),
    )
    style.configure(
        "Treeview.Heading",
        background=COLOR_ACCENTO,
        foreground="white",
        font=("Segoe UI", 10, "bold"),
    )
    style.map("Treeview.Heading", background=[("active", COLOR_ACCENTO_HOVER)])
