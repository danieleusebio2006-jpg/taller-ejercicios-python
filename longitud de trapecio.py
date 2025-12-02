def capturar():
    """
    Captura la base mayor, la base menor y la altura del trapecio desde el usuario.
    Retorna un diccionario con la base mayor, la base menor y la altura.
    """
    base_mayor = float(input("Ingrese la longitud de la base mayor del trapecio: "))
    base_menor = float(input("Ingrese la longitud de la base menor del trapecio: "))
    altura = float(input("Ingrese la altura del trapecio: "))
    return {"base_mayor": base_mayor, "base_menor": base_menor, "altura": altura}

def procesar(datos):
    """
    Calcula el área del trapecio a partir de las longitudes de sus bases y su altura.
    Recibe un diccionario con la base mayor, la base menor y la altura.
    Retorna el área del trapecio.
    """
    base_mayor = datos["base_mayor"]
    base_menor = datos["base_menor"]
    altura = datos["altura"]
    area = ((base_mayor + base_menor) / 2) * altura
    return area

def imprimir_datos(area):
    """
    Imprime el área del trapecio.
    Recibe el área del trapecio.
    """
    print(f"El área del trapecio es: {area}")

# Programa principal
datos = capturar()
area = procesar(datos)
imprimir_datos(area)
