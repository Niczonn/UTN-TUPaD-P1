hemisferio = input("En qué hemisferio se encuentra (N/S)? ")
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))

if hemisferio.upper() == "N":
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2 and dia <= 20):
        print("Invierno")
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5 and dia <= 20):
        print("Primavera")
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8 and dia <= 20):
        print("Verano")
    elif (mes == 9 and dia >= 21) or (10 <= mes <= 11 and dia <= 20):
        print("Otoño")
else:
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2 and dia <= 20):
        print("Verano")
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5 and dia <= 20):
        print("Otoño")
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8 and dia <= 20):
        print("Invierno")
    elif (mes == 9 and dia >= 21) or (10 <= mes <= 11 and dia <= 20):
        print("Primavera")