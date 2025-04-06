numero1 = int(input("Ingresa el primer número (distinto de 0): "))
numero2 = int(input("Ingresa el segundo número (distinto de 0): "))

if numero1 != 0 and numero2 != 0:
    suma = numero1 + numero2
    division = numero1 / numero2
    multiplicacion = numero1 * numero2
    resta = numero1 - numero2
    
    print(f"Suma: {suma}")
    print(f"División: {division}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"Resta: {resta}")
else:
    print("Por favor, ingresa números distintos de 0.")