import tkinter as tk    

ventana = tk.Tk()
ventana.title("Ventana 1")
ventana.geometry("400x400")

ventana2= tk.Toplevel()
ventana2.title("Ventana 2") 
ventana2.geometry("400x600")
ventana2.withdraw()  


tk.Label(ventana, text="Bienvenido a la ventana 1").pack(pady=10)
tk.Button(ventana, 
          text="Abrir ventana 2",
          command=lambda: (ventana.withdraw, ventana2.deiconify())).pack()     

tk.Label (ventana2, text="Bienvenido a la ventana 2").pack()
tk.Button(ventana2, 
          text="Volver a la ventana 1", 
            command=lambda: (ventana2.withdraw, ventana.deiconify())).pack()


def_cambiar_color = lambda: ventana2.configure(bg="lightblue", pady=10) 
tk.Button(ventana2,
          text="Cambiar color de fondo", 
          command=def_cambiar_color).pack(pady=10)                  

        
ventana.mainloop()
