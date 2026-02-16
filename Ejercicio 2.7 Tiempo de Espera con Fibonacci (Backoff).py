# Cálculo del tiempo de espera según Fibonacci
n = int(input("Ingrese el número de reintento (1..): "))

if n <= 0:
    print("El número debe ser positivo")
else:
    a, b = 1, 1
    for i in range(3, n + 1):
        a, b = b, a + b
    if n == 1 or n == 2:
        resultado = 1
    else:
        resultado = b
    print(f"Tiempo de espera: {resultado} segundos")