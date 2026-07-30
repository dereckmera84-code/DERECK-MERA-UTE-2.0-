from registro import VentanaRegistro
from opciones import VentanaOpciones 
def main():
 ferre = VentanaRegistro(imagen_path="santa_lucia.jpg")
 ferre.ventana_opciones = VentanaOpciones(ferre)
 ferre.ventana_opciones.withdraw()
 ferre.mainloop() 
 
if __name__ == "__main__":
 main()
 
