def capturar():
    """
    Captura la temperatura en grados Celsius desde el usuario.
    Retorna la temperatura en Celsius.
    """
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    return celsius

def procesar(celsius):
    """
    Convierte la temperatura de Celsius a Fahrenheit.
    Recibe la temperatura en Celsius.
    Retorna la temperatura en Fahrenheit.
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def imprimir_datos(fahrenheit):
    """
    Imprime la temperatura en grados Fahrenheit.
    Recibe la temperatura en Fahrenheit.
    """
    print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")

# Programa principal
celsius = capturar()
fahrenheit = procesar(celsius)
imprimir_datos(fahrenheit)