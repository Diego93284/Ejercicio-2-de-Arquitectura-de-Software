# Clasificador de triángulos por ángulos
a1 = int(input("Ingrese ángulo 1: "))
a2 = int(input("Ingrese ángulo 2: "))
a3 = int(input("Ingrese ángulo 3: "))

if a1 + a2 + a3 != 180:
    print("No es un triángulo válido (la suma debe ser 180°)")
else:
    if a1 == a2 == a3:
        print("Equilátero")
    elif a1 == 90 or a2 == 90 or a3 == 90:
        print("Ángulo Recto")
    elif a1 == a2 or a1 == a3 or a2 == a3:
        print("Isósceles")
    else:
        print("Escaleno")