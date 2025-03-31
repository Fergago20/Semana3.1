# Ejercicio 1
import statistics

class Edad:
    def __init__(self, edades):
        self.edadades = edades

    def _calcular_media(self):
        return sum(self.edadades)/len(self.edadades)
    
    def mostrar_media(self):
        media = self._calcular_media()
        return f"La media de las edades es: {media:.2f} años"
    
    def calc_media(self):
        return statistics.mean(self.edadades)
    
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

    if not edades:
        print("No se han introducido edades.")
        return
    else:
        edad_obj = Edad(edades)
        print(edad_obj.mostrar_media())
        print(f"La media de las edades es: {edad_obj.calc_media():.2f} años")

if __name__ == "__main__":
    main()