def capturar():
    """
    Captura la base y la altura del paralelogramo desde el usuario.
    Retorna un diccionario con la base y la altura.
    """
    base = float(input("Ingrese la longitud de la base del paralelogramo: "))
    altura = float(input("Ingrese la altura del paralelogramo: "))
    return {"base": base, "altura": altura}

def procesar(datos):
    """
    Calcula el área del paralelogramo a partir de la base y la altura.
    Recibe un diccionario con la base y la altura.
    Retorna el área del paralelogramo.
    """
    base = datos["base"]
    altura = datos["altura"]
    area = base * altura
    return area

def imprimir_datos(area):
    """
    Imprime el área del paralelogramo.
    Recibe el área del paralelogramo.
    """
    print(f"El área del paralelogramo es: {area}")

# Programa principal
datos = capturar()
area = procesar(datos)
imprimir_datos(area)