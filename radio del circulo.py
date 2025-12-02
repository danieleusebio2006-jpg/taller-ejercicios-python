import math

def capturar():
    """
    Captura el radio del círculo desde el usuario.
    Retorna el radio.
    """
    radio = float(input("Ingrese el radio del círculo: "))
    return radio

def procesar(radio):
    """
    Calcula el área del círculo a partir del radio.
    Recibe el radio del círculo.
    Retorna el área del círculo.
    """
    area = math.pi * (radio ** 2)
    return area

def imprimir_datos(area):
    """
    Imprime el área del círculo.
    Recibe el área del círculo.
    """
    print(f"El área del círculo es: {area}")

# Programa principal
radio = capturar()
area = procesar(radio)
imprimir_datos(area)