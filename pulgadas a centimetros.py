def capturar():
    """
    Captura la longitud en pulgadas desde el usuario.
    Retorna la longitud en pulgadas.
    """
    pulgadas = float(input("Ingrese la longitud en pulgadas: "))
    return pulgadas

def procesar(pulgadas):
    """
    Convierte la longitud de pulgadas a centímetros.
    Recibe la longitud en pulgadas.
    Retorna la longitud en centímetros.
    """
    centimetros = pulgadas * 2.54
    return centimetros

def imprimir_datos(centimetros):
    """
    Imprime la longitud en centímetros.
    Recibe la longitud en centímetros.
    """
    print(f"La longitud en centímetros es: {centimetros}")

# Programa principal
pulgadas = capturar()
centimetros = procesar(pulgadas)
imprimir_datos(centimetros)