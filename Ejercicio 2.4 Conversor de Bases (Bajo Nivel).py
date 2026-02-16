# Conversión a binario y hexadecimal sin funciones integradas
n = int(input("Ingrese un número decimal: "))
original = n

# Binario manual
if n == 0:
    binario = "0"
else:
    binario = ""
    while n > 0:
        binario = str(n % 2) + binario
        n //= 2

# Hexadecimal manual
n = original
if n == 0:
    hexa = "0"
else:
    digitos = "0123456789ABCDEF"
    hexa = ""
    while n > 0:
        hexa = digitos[n % 16] + hexa
        n //= 16

print(f"Binario: {binario}")
print(f"Hexadecimal: {hexa}")