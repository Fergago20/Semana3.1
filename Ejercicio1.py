# Ejercicio 1

class Edad:
    def __init__(self, edades):
        self.edadades = edades

    def _calcular_media(self):
        return sum(self.edadades)/len(self.edadades)
    
    def mostrar_media(self):
        media = self._calcular_media()
        return f"La media de las edades es: {media:.2f} años"
    
def main():
    edades = []
    while True:
        try:
            edad=(int(input("Introduce una edad (o -1 para terminar): ")))
            if edad == -1:
                break
            edades.append(edad)
            
        except ValueError as e:
            print(f"Error: {e}. Por favor, introduce edades válidas.")

    edad_obj = Edad(edades)
    print(edad_obj.mostrar_media())

if __name__ == "__main__":
    main()