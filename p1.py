import tkinter as tk
ventana = tk.Tk()
ventana.title("Ingreso de datos")
ventana.geometry("400x400") 

tk.Label(ventana, text="Nombre:").pack()

entrada_nombre=tk.Entry(ventana)
entrada_nombre.pack(pady=10)    

tk.Label(ventana, text="Edad:").pack()
entrada_edad = tk.Entry(ventana)
entrada_edad.pack(pady=10)  

tk.Label(ventana, text="Género:").pack()
genero_var = tk.StringVar()
genero_var.set("No especificado")
tk.Radiobutton(ventana, text="Masculino", variable=genero_var, value="Masculino").pack()
tk.Radiobutton(ventana, text="Femenino", variable=genero_var, value="Femenino").pack()
tk.Radiobutton(ventana, text="Otro", variable=genero_var, value="Otro").pack()

tk.Button(ventana,
          text= "Registrar",
          command=lambda:print
          ({"Nombre": entrada_nombre.get(), 
            "Edad": entrada_edad.get(), 
            "Género": genero_var.get()}))





ventana.mainloop()
