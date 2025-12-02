def capturar():
    """
    Captura la longitud del lado del cuadrado desde el usuario.
    Retorna la longitud del lado.
    """
    lado = float(input("Ingrese la longitud del lado del cuadrado: "))
    return lado

def procesar(lado):
    """
    Calcula el área del cuadrado a partir de la longitud del lado.
    Recibe la longitud del lado.
    Retorna el área del cuadrado.
    """
    area = lado ** 2
    return area

def imprimir_datos(area):
    """
    Imprime el área del cuadrado.
    Recibe el área del cuadrado.
    """
    print(f"El área del cuadrado es: {area}")

# Programa principal
lado = capturar()
area = procesar(lado)
imprimir_datos(area)