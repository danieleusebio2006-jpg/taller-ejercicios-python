def capturar():
    """
    Captura la longitud del lado del cubo desde el usuario.
    Retorna la longitud del lado.
    """
    lado = float(input("Ingrese la longitud del lado del cubo: "))
    return lado

def procesar(lado):
    """
    Calcula el volumen del cubo a partir de la longitud del lado.
    Recibe la longitud del lado.
    Retorna el volumen del cubo.
    """
    volumen = lado ** 3
    return volumen

def imprimir_datos(volumen):
    """
    Imprime el volumen del cubo.
    Recibe el volumen del cubo.
    """
    print(f"El volumen del cubo es: {volumen}")

# Programa principal
lado = capturar()
volumen = procesar(lado)
imprimir_datos(volumen)