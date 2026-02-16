# Checksum por suma ASCII
mensaje = input("Ingrese el mensaje: ")
suma = 0
for c in mensaje:
    suma += ord(c)
print("Suma ASCII:", suma)
print("¿Paquete íntegro (suma par)?", suma % 2 == 0)