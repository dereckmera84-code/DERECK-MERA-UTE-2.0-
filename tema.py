
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
