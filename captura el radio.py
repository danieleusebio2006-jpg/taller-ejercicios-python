import math
def capturar():
#capturar el radio de la esfera desde el usuario
 #retorna el radio
    radio=float(input("ingrese el radio de la esfera: "))
    return radio  



 #calcular el volumen de la esfera a partir del radio
  #recibe el radio de la esfera
  
volumen = (4/3) * math.pi * (radio)

return volumen
def imprimir_datos(volumen):

 #imprime el volumen de la esfera
  #recibe el volumen de la esfera
 print(f"el volumen de la esfera es:{volumen}")
