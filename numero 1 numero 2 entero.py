# Solicitar al usuario que ingrese dos números
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

# Calcular la diferencia entre los dos números
diferencia = numero1 - numero2

# Determinar el mayor usando la diferencia
if diferencia > 0:
    mayor = numero1
else:
    mayor = numero2

# Mostrar el resultado
print("El número mayor es:", mayor)