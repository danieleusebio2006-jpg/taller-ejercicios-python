import math

def capturar():
    """
    Captura la longitud del lado del hexágono regular desde el usuario.
    Retorna la longitud del lado.
    """
    lado = float(input("Ingrese la longitud del lado del hexágono regular: "))
    return lado

def procesar(lado):
    """
    Calcula el área del hexágono regular a partir de la longitud del lado.
    Recibe la longitud del lado.
    Retorna el área del hexágono regular.
    """
    area = (3 * math.sqrt(3) * lado**2) / 2
    return area

def imprimir_datos(area):
    """
    Imprime el área del hexágono regular.
    Recibe el área del hexágono regular.
    """
    print(f"El área del hexágono regular es: {area}")

# Programa principal
lado = capturar()
area = procesar(lado)
imprimir_datos(area)