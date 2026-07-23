opcion_var = tk.IntVar()
check = tk.Checkbutton(ventana, 
                     text="activar modo oscuro", 
                     variable=opcion_var, 
                     font=("Arial",14))
check.pack(pady=10)


genero_var=tk.StringVar()
genero_var.set("Ninguno")

tk.Label(ventana, text="Selecciona tu género:").pack()
tk.Radiobutton(ventana, 
               text="Masculino", 
               variable=genero_var, 
               value="Masculino").pack()
tk.Radiobutton(ventana, 
               text="Femenino",
               variable=genero_var, 
               value="Femenino").pack()
tk.Radiobutton(ventana, 
               text="Otro", 
               variable=genero_var, 
               value="Otro").pack()

#Listbox
tk.Label(ventana, text="Selecciona una fruta:").pack()
lista = tk.Listbox(ventana)
lista.insert(tk.END, "Manzana")
lista.insert(tk.END, "Banana")
lista.insert(tk.END, "Naranja")
lista.insert(tk.END, "Pera") 
lista.insert(tk.END, "Uva")
lista.pack(pady=10)



ventana.mainloop()
