print("hola mundo")

#ejercicio2
nombre = input("¿Cuál es tu nombre? ")
print(f"Hola {nombre}!")

#ejercicio3
nombre = input("¿Cuál es tu nombre? ")
apellido = input("¿Cuál es tu apellido? ")
edad = input("¿Cuántos años tienes? ")
lugar = input("¿Dónde vives? ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}.")

#ejercicio4
import math

radio = float(input("Ingresa el radio del círculo: "))
area = math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

#ejercicio5
segundos = int(input("Ingresa la cantidad de segundos: "))
horas = segundos // 3600
segundos_restantes = segundos % 3600
print(f"{segundos} segundos equivalen a {horas} horas y {segundos_restantes} segundos.")

#ejercicio6
numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
    
#ejercicio7
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
    
#ejercicio8
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))
imc = peso / (altura ** 2)
print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")

#ejercicio9+
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} grados Celsius equivalen a {fahrenheit:.2f} grados Fahrenheit.")


#ejercicio10
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los tres números es: {promedio:.2f}")



