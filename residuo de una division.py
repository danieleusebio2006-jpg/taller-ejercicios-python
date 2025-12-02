# Solicitar al usuario que ingrese el dividendo (entero)
dividendo = int(input("Ingresa el dividendo (entero): "))

# Solicitar al usuario que ingrese el divisor (entero)
divisor = int(input("Ingresa el divisor (entero): "))

# Verificar si el divisor es cero
if divisor == 0:
    print("Error: No se puede dividir entre cero.")
else:
    # Calcular el residuo
    residuo = dividendo % divisor

    # Mostrar el resultado
    print("El residuo de la división es:", residuo)