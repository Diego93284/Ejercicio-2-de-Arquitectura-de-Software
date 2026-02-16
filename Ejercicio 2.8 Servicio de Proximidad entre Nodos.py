import math

# Distancia euclidiana y proximidad
x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Distancia:", round(distancia, 2))
print("¿Están a menos de 10 unidades?", distancia < 10)