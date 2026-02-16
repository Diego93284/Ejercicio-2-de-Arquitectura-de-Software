# Rate limiter según tipo de usuario y mantenimiento
tipo = input("Tipo de usuario (Premium/Standard): ").capitalize()
mantenimiento = input("¿Servidor en mantenimiento? (s/n): ").lower() == 's'

if mantenimiento:
    limite = 0
else:
    if tipo == "Premium":
        limite = 1000
    elif tipo == "Standard":
        limite = 100
    else:
        limite = 0

print("Límite de peticiones:", limite)