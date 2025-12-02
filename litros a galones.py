def capturar():
    """
    Captura la cantidad en litros desde el usuario.
    Retorna la cantidad en litros.
    """
    litros = float(input("Ingrese la cantidad en litros: "))
    return litros

def procesar(litros):
    """
    Convierte la cantidad de litros a galones.
    Recibe la cantidad en litros.
    Retorna la cantidad en galones.
    """
    galones = litros * 0.264172
    return galones

def imprimir_datos(galones):
    """
    Imprime la cantidad en galones.
    Recibe la cantidad en galones.
    """
    print(f"La cantidad en galones es: {galones}")

# Programa principal
litros = capturar()
galones = procesar(litros)
imprimir_datos(galones)