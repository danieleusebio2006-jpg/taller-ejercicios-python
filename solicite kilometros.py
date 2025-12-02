# Solicitar la distancia en kilómetros
kilometros = float(input("Ingresa la distancia en kilómetros: "))

# Factor de conversión
factor_conversion = 0.621371

# Calcular la distancia en millas
millas = kilometros * factor_conversion

# Mostrar el resultado
print(kilometros, "kilómetros equivalen a", millas, "millas")