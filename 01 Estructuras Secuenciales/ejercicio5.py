segundos = int(input("Ingresa la cantidad de segundos: "))
horas = segundos // 3600
segundos_restantes = segundos % 3600
print(f"{segundos} segundos equivalen a {horas} horas y {segundos_restantes} segundos.")