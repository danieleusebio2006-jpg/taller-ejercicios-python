def capturar():
    """
    Captura la cantidad en libras desde el usuario.
    Retorna la cantidad en libras.
    """
    libras = float(input("Ingrese la cantidad en libras: "))
    return libras

def procesar(libras):
    """
    Convierte la cantidad de libras a kilogramos.
    Recibe la cantidad en libras.
    Retorna la cantidad en kilogramos.
    """
    kilogramos = libras * 0.45359237
    return kilogramos

def imprimir_datos(kilogramos):
    """
    Imprime la cantidad en kilogramos.
    Recibe la cantidad en kilogramos.
    """
    print(f"La cantidad en kilogramos es: {kilogramos}")

# Programa principal
libras = capturar()
kilogramos = procesar(libras)
imprimir_datos(kilogramos)