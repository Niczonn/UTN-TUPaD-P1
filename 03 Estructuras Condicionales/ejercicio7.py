frase = input("Ingrese una frase o palabra: ")
vocales = "aeiouAEIOU"
if frase[-1] in vocales:
    print(frase + "!")
else:
    print(frase)