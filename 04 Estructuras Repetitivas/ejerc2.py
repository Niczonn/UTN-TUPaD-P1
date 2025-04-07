numero = int(input("Ingresa un número entero: "))
cantidad_digitos = len(str(abs(numero)))  # abs para números negativos
print("La cantidad de dígitos es:", cantidad_digitos)