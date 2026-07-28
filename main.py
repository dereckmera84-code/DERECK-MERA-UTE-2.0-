from registro import VentanaRegistro
from opciones import VentanaOpciones
 
def main():
 app = VentanaRegistro(imagen_path="santa_lucia.jpg")
 app.ventana_opciones = VentanaOpciones(app)
 app.mainloop() 
 
if __name__ == "__main__":
 main()
 
