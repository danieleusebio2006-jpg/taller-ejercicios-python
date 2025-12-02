# Solicitar el precio del artículo
precio = float(input("Ingresa el precio del artículo: "))

# Calcular el descuento (10%)
descuento = precio * 0.10

# Calcular el precio final (precio - descuento)
precio_final = precio - descuento

# Mostrar el resultado
print("El precio original es:", precio)
print("El descuento del 10% es:", descuento)
print("El precio final con descuento es:", precio_final)