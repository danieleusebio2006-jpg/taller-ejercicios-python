def capturar():
    """
    Captura la longitud, el ancho y la altura del prisma rectangular desde el usuario.
    Retorna un diccionario con estos valores.
    """
    longitud = float(input("Ingrese la longitud del prisma rectangular: "))
    ancho = float(input("Ingrese el ancho del prisma rectangular: "))
    altura = float(input("Ingrese la altura del prisma rectangular: "))
    return {"longitud": longitud, "ancho": ancho, "altura": altura}

def procesar(datos):
    """
    Calcula el volumen del prisma rectangular.
    Recibe un diccionario con la longitud, el ancho y la altura.
    Retorna el volumen.
    """
    longitud = datos["longitud"]
    ancho = datos["ancho"]
    altura = datos["altura"]
    volumen = longitud * ancho * altura
    return volumen

def imprimir_datos(volumen):
    """
    Muestra el volumen del prisma rectangular.
    """
    print(f"El volumen del prisma rectangular es: {volumen}")

# Programa principal
datos = capturar()
volumen = procesar(datos)
imprimir_datos(volumen)