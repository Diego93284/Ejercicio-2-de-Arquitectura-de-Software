# Auditor de latencias
tiempos = list(map(int, input("Ingrese tiempos de respuesta separados por espacio: ").split()))
umbral = int(input("Ingrese umbral crítico: "))

if tiempos:
    promedio = sum(tiempos) / len(tiempos)
    alerta = promedio > umbral
    for t in tiempos:
        if t > 3 * promedio:
            alerta = True
            break
    print("¿Alerta?", alerta)
else:
    print("Lista vacía, no se puede evaluar")