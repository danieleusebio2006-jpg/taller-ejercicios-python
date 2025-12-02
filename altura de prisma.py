def capturar():
    """
    Captura la longitud de la base, la altura y el ancho del prisma triangular desde el usuario.
    Retorna un diccionario con la longitud de la base, la altura y el ancho.
    """
    longitud_base = float(input("Ingrese la longitud de la base del triángulo: "))
    altura_triangulo = float(input("Ingrese la altura del triángulo: "))
    ancho_prisma = float(input("Ingrese el ancho del prisma: "))
    return {"longitud_base": longitud_base, "altura_triangulo": altura_triangulo, "ancho_prisma": ancho_prisma}

def procesar(datos):
    """
    Calcula el volumen del prisma triangular a partir de la longitud de la base, la altura y el ancho.
    Recibe un diccionario con la longitud de la base, la altura y el ancho.
    Retorna el volumen del prisma triangular.
    """
    longitud_base = datos["longitud_base"]
    altura_triangulo = datos["altura_triangulo"]
    ancho_prisma = datos["ancho_prisma"]
    area_triangulo = 0.5 * longitud_base * altura_triangulo
    volumen = area_triangulo * ancho_prisma
    return volumen

def imprimir_datos(volumen):
    """
    Imprime el volumen del prisma triangular.
    Recibe el volumen del prisma triangular.
    """
    print(f"El volumen del prisma triangular es: {volumen}")

# Programa principal
datos = capturar()
volumen = procesar(datos)
imprimir_datos(volumen)