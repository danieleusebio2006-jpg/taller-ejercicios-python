# Solicitar al usuario que ingrese el primer número (dividendo)
dividendo = float(input("Ingresa el dividendo: "))

# Solicitar al usuario que ingrese el segundo número (divisor)
divisor = float(input("Ingresa el divisor: "))

# Verificar si el divisor es cero
if divisor == 0:
    print("Error: No se puede dividir entre cero.")
else:
    # Calcular la división
    resultado = dividendo / divisor

    # Mostrar el resultado
    print("El resultado de la división es:", resultado)