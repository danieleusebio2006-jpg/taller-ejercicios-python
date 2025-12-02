import math

def capturar():
    """
    Captura el radio de la base y la altura del cono desde el usuario.
    Retorna un diccionario con el radio y la altura.
    """
    radio = float(input("Ingrese el radio de la base del cono: "))
    altura = float(input("Ingrese la altura del cono: "))
    return {"radio": radio, "altura": altura}

def procesar(datos):
    """
    Calcula el volumen del cono a partir del radio y la altura.
    Recibe un diccionario con el radio y la altura.
    Retorna el volumen del cono.
    """
    radio = datos["radio"]
    altura = datos["altura"]
    volumen = (1/3) * math.pi * (radio ** 2) * altura
    return volumen

def imprimir_datos(volumen):
    """
    Imprime el volumen del cono.
    Recibe el volumen del cono.
    """
    print(f"El volumen del cono es: {volumen}")

# Programa principal
datos = capturar()
volumen = procesar(datos)
imprimir_datos(volumen)