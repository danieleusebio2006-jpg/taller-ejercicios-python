def capturar():
    """
    Captura la distancia en kilómetros desde el usuario.
    Retorna la distancia en kilómetros.
    """
    kilometros = float(input("Ingrese la distancia en kilómetros: "))
    return kilometros

def procesar(kilometros):
    """
    Convierte la distancia de kilómetros a millas.
    Recibe la distancia en kilómetros.
    Retorna la distancia en millas.
    """
    millas = kilometros * 0.621371
    return millas

def imprimir_datos(millas):
    """
    Imprime la distancia en millas.
    Recibe la distancia en millas.
    """
    print(f"La distancia en millas es: {millas}")

# Programa principal
kilometros = capturar()
millas = procesar(kilometros)
imprimir_datos(millas)