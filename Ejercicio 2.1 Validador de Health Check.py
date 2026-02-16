# Health Check Validator
latencia = int(input("Ingrese latencia (ms): "))
cpu = int(input("Ingrese uso de CPU (%): "))
db_conectada = input("¿Base de datos conectada? (s/n): ").lower() == 's'

saludable = latencia < 200 and cpu < 80 and db_conectada
print("Resultado:", saludable)