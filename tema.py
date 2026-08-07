def aplicar_tema(style):

 style.theme_use("clam")
 style.configure("Fondo.TFrame",background="#0F2E52")
 style.configure("Titulo.Tlabel",
 background="#0F2E52",
 foreground="#9FBFE2",
 font=("segoe UI",12))

 style.configure("Texto.Tlabel",
 background="#0F2E52",
 foreground="#EAF1FB",
 font=("segoe UI",12))

 style.configure("Estado.Tlabel",
 background="#0F2E52",
 font=("segoe UI",11,"bold"))

 style.configure("TEntry",
 fieldbackground="#FAFBFD",
 padding=6,
 font=("segoe UI",12))
 style.configure("Tcheckbutton",
 background="#0F2E52",
 foreground="#EAF1FB",
 font=("segoe UI",12))

 style.map("Tcheckbutton",
 background=[("active","#0F2E52")])
 
 style.configure("TRadiobutton",
 background="#0F2E52",
 foreground="#FAFBFD",
 font=("segoe UI",12))

 style.map("TRadiobutton",
 background=[("active","#2966AC")])

 style.configure("Accent.Tbutton",
 background="#466991",
 foreground="#FAFBFD",
 font=("segoe UI",12,"bold"),
 padding=(14, 8),
 borderwidth=0)

 style.map("accent.Tbutton",
 background=["active", "#3A7BC8"])

 style.configure("Secondary.Tbutton",
 background="#9FBFE2",
 foreground="#0F2E52",
 font=("segoe UI", 11),
 padding=(14, 8),
 borderwidth=0)

 style.map("secondary.Tbutton",
 background=["active","#C3D8F0"])

 style.configure("treeview",
 background="#FAFBFD",
 fieldbackground="#FAFBFD",
 foreground="#1A1A1A",
 rowheight=25,
 font=("segoe UI", 10))

 style.map("treeview.header",
background=[("active", "#3A7BC8")])
 
 style.configure("treeview.header",
 background= "#2966AC",
 foreground="#FAFBFD",
 font=("segoe UI",11, "bold"))
