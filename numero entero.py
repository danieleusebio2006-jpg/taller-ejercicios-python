# Solicitar al usuario que ingrese un número entero
numero = int(input("Ingresa un número: "))

# Verificar si el número es par o impar
if numero % 2 == 0:
    print("El número", numero, "es par.")
else:
    print("El número", numero, "es impar.")