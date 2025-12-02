# Solicitar el saldo de la cuenta
saldo = float(input("Ingresa el saldo de la cuenta: "))

# Tasa de interés (5%)
tasa_interes = 0.05

# Calcular el interés
interes = saldo * tasa_interes

# Calcular el saldo final
saldo_final = saldo + interes

# Mostrar los resultados
print("El interés ganado es:", interes)
print("El saldo final es:", saldo_final)