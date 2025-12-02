def capturar():
    """
    Captura la cantidad en dólares y la tasa de cambio desde el usuario.
    Retorna un diccionario con la cantidad en dólares y la tasa de cambio.
    """
    dolares = float(input("Ingrese la cantidad en dólares: "))
    tasa_cambio = float(input("Ingrese la tasa de cambio (dólares a euros): "))
    return {"dolares": dolares, "tasa_cambio": tasa_cambio}

def procesar(datos):
    """
    Convierte la cantidad de dólares a euros utilizando la tasa de cambio.
    Recibe un diccionario con la cantidad en dólares y la tasa de cambio.
    Retorna la cantidad en euros.
    """
    dolares = datos["dolares"]
    tasa_cambio = datos["tasa_cambio"]
    euros = dolares * tasa_cambio
    return euros

def imprimir_datos(euros):
    """
    Imprime la cantidad en euros.
    Recibe la cantidad en euros.
    """
    print(f"La cantidad en euros es: {euros}")

# Programa principal
datos = capturar()
euros = procesar(datos)
imprimir_datos(euros)