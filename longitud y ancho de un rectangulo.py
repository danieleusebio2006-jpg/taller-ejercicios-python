def capturar():
    """
    Captura la longitud y el ancho del rectángulo desde el usuario.
    Retorna un diccionario con la longitud y el ancho.
    """
    longitud = float(input("Ingrese la longitud del rectángulo: "))
    ancho = float(input("Ingrese el ancho del rectángulo: "))
    return {"longitud": longitud, "ancho": ancho}

def procesar(datos):
    """
    Calcula el área del rectángulo a partir de la longitud y el ancho.
    Recibe un diccionario con la longitud y el ancho.
    Retorna el área del rectángulo.
    """
    longitud = datos["longitud"]
    ancho = datos["ancho"]
    area = longitud * ancho
    return area

def imprimir_datos(area):
    """
    Imprime el área del rectángulo.
    Recibe el área del rectángulo.
    """
    print(f"El área del rectángulo es: {area}")

# Programa principal
datos = capturar()
area = procesar(datos)
imprimir_datos(area)