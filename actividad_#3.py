# crear una funcion que se llame numero mayor y recibe 2 parametros numero 1 y numero 2, y que devuelva el numero mayor de alguno de esos 2.
def numero_mayor(numero1,numero2):
    if numero1>numero2:
        return numero1
    elif numero1<numero2:
        return numero2
    else: 
        return f"{numero1} y {numero2} son iguales"
print(numero_mayor(5,5))

# Crear una función que se llame longitud cadena y devuelva la cantidad de caracteres de la cadena de texto.

def longitud_cadena(cadena):
    return f"{len(cadena)} es la cantidad de caracteres"
print(longitud_cadena("diez"))
    
# Crear una función que se llame sumar pares y reciba un parametro este parametro se va a llamar numero y dentro de la funcion tiene que existir 5 variables y que cada variable tenga un numero del 1 al 5 y sumar solamente los pares.

def sumar_pares(numero):
    numero1=1
    numero2=2
    numero3=3
    numero4=4
    numero5=5
    if numero%2==0:
        return numero2+numero4+numero
    else:
        return numero1+numero3+numero5
print(sumar_pares(5))

