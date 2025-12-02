def capturar():
    """
    Captura la longitud de la base, el ancho de la base y la altura de la pirámide desde el usuario.
    Retorna un diccionario con la longitud de la base, el ancho de la base y la altura.
    """
    longitud_base = float(input("Ingrese la longitud de la base de la pirámide: "))
    ancho_base = float(input("Ingrese el ancho de la base de la pirámide: "))
    altura = float(input("Ingrese la altura de la pirámide: "))
    return {"longitud_base": longitud_base, "ancho_base": ancho_base, "altura": altura}

def procesar(datos):
    """
    Calcula el volumen de la pirámide a partir de la longitud de la base, el ancho de la base y la altura.
    Recibe un diccionario con la longitud de la base, el ancho de la base y la altura.
    Retorna el volumen de la pirámide.
    """
    longitud_base = datos["longitud_base"]
    ancho_base = datos["ancho_base"]
    altura = datos["altura"]
    volumen = (1/3) * longitud_base * ancho_base * altura
    return volumen

def imprimir_datos(volumen):
    """
    Imprime el volumen de la pirámide.
    Recibe el volumen de la pirámide.
    """
    print(f"El volumen de la pirámide es: {volumen}")

# Programa principal
datos = capturar()
volumen = procesar(datos)
imprimir_datos(volumen)