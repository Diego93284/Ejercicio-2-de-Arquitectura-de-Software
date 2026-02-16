# Validador de token
token = input("Ingrese el token: ")
valido = True

if len(token) <= 12:
    valido = False
else:
    tiene_numero = False
    for c in token:
        if c.isdigit():
            tiene_numero = True
            break
    if not tiene_numero:
        valido = False
    elif token.startswith("TEST"):
        valido = False

print("Token válido?" , valido)