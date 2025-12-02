# Solicitar los números
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

# Verificar si el segundo número es cero para evitar división por cero
if numero2 == 0:
    print("El segundo número no puede ser cero.")
else:
    # Verificar si numero1 es múltiplo de numero2
    if numero1 % numero2 == 0:
        print(numero1, "es múltiplo de", numero2)
    else:
        print(numero1, "no es múltiplo de", numero2)