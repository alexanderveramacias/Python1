numero=int(input("ingrese un número: "))
if numero>=0:
    print("el número ingresado es mayor o igual a cero")
elif numero<0:
    print("el número ingresado es negativo")
else:
    print("no ingresaste un número")


# ejercicio_2
numero1=int(input("ingrese un número: "))
for index in range(0,numero1):
    print(numero1)

# ejercicio_3
texto_usuario=input("introducir un texto: ")
for caracter in texto_usuario:
    print(caracter)
