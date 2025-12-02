# capturar la base y la altura del triangulo desde el usuario
  # retorna un diccionario con la base y la altura

def capturar():
    base= float(input("ingrese la base del triangulo:"))
    altura=float(input("ingrese la altura del triangulo:"))
    return{"base": base,"altura": altura}
    
# calcular el area del triangulo a partir de la base y la altura
  #recibe un diccionario con la base y la altura 
    #retorna el area del triangulo

    def procesar(datos):
        base= datos["base"]
        altura= datos["altura"]
        area= (base * altura) / 2
        return area

#imprime el area del triangulo
#recibe el area del triangulo

def imprimir_datos(area):
    print(f"el area del triangulo es:{area}") 

    #programa principal 
    datos=capturar()
    area=procesar(datos)
    imprimir_datos(area)

