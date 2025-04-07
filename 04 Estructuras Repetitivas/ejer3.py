valor1 = int(input("Ingresa el primer número: "))
valor2 = int(input("Ingresa el segundo número: "))
total = 0
for i in range(valor1 + 1, valor2):
    total += i
print("La suma es:", total)