import math

def capturar():
    """
    Captura el radio de la base y la altura del cilindro desde el usuario.
    Retorna un diccionario con el radio y la altura.
    """
    radio = float(input("Ingrese el radio de la base del cilindro: "))
    altura = float(input("Ingrese la altura del cilindro: "))
    return {"radio": radio, "altura": altura}

def procesar(datos):
    """
    Calcula el volumen del cilindro a partir del radio y la altura.
    Recibe un diccionario con el radio y la altura.
    Retorna el volumen del cilindro.
    """
    radio = datos["radio"]
    altura = datos["altura"]
    volumen = math.pi * (radio ** 2) * altura
    return volumen

def imprimir_datos(volumen):
    """
    Imprime el volumen del cilindro.
    Recibe el volumen del cilindro.
    """
    print(f"El volumen del cilindro es: {volumen}")

# Programa principal
datos = capturar()
volumen = procesar(datos)
imprimir_datos(volumen)