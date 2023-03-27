# escribir una función llamada rectangulo y que esta reciba un parametro llamado perimetro y altura y esta función me va a devolver el perimetro y la altura del rectangulo
# escribir una función que reciba un parametro llamado admin y validar el administrador y que me devuelva true o false si el administrador es correcto o incorrecto,
# escribir una función que se llame raiz cuadrada y que reciba un parametro llamado número y me devuelva el resultado y determinar si el valor ingresado no es un numero.

def rectangulo(perimetro,altura):
    resultado_perimetro=perimetro+altura
    altura_rectangulo=altura
    return f"el perimetro del rectangulo es {resultado_perimetro} y la altura es  {altura_rectangulo}"
print(rectangulo(13,9))

def administrador(admin):
    if admin == "alex":
        return True
    else:
        return False
print(administrador("tomas"))

def raiz_cuadrada(numero):
    numero**0.5
    resultado=numero**0.5
    return resultado
print(raiz_cuadrada(4))


