# Calculadora con operaciones básicas y avanzadas
print("Operaciones: suma, resta, multiplicacion, division, fibonacci, conversion")
op = input("Ingrese operación: ").lower()

if op in ["suma", "resta", "multiplicacion", "division"]:
    a = float(input("Ingrese primer número: "))
    b = float(input("Ingrese segundo número: "))
    if op == "suma":
        print("Resultado:", a + b)
    elif op == "resta":
        print("Resultado:", a - b)
    elif op == "multiplicacion":
        print("Resultado:", a * b)
    elif op == "division":
        if b == 0:
            print("Error: división por cero")
        else:
            print("Resultado:", a / b)

elif op == "fibonacci":
    n = int(input("¿Cuántos números de Fibonacci desea generar?: "))
    if n <= 0:
        print("Ingrese un número positivo")
    else:
        fib = [1, 1]
        for i in range(2, n):
            fib.append(fib[-1] + fib[-2])
        print("Serie Fibonacci:", fib[:n])

elif op == "conversion":
    num = int(input("Ingrese número decimal: "))
    print("Binario:", bin(num)[2:])
    print("Hexadecimal:", hex(num)[2:].upper())
else:
    print("Operación no válida")