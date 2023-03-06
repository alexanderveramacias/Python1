#operadores aritmeticos
print(2+2)
print(2*2)
print(2-2)
print(2/2)
#operadores lógicos
print(1<2)
print(2>1)
print(3>=4)
print(7>=7)
print(7<=7)
print(7 != 7)
print("hola mundo"==4)
if 7<6:
    print("siete es mayor")
else: 
    print("7 no es mayor")
#input("ingresa el admin: ")
nnn=input("ingresa el admin: ")
if nnn=="alex":
    print("yo soy el administrador")
else:
    print("la persona ingresada no es el administrador")   
if nnn=="ALEX":
    print("no es el administrador")
else:
    print("administrador bienvenido") 
    print(f"eres {nnn}")   

    num=int(input("ingresa un número: "))
if num>0:
    print(f"este número no es negativo {num}")
else: 
    num<0
    print(f"es un número negativo {num}") 

sss=int(input("no se permite números mayores a 7"))
if sss>7:
   print(f"este número es mayor a 7 {sss}") 
else:
    sss<7
    print(f"este número es menor a 7 {sss}")

# operadores relacionales
# and
# or
# not
print(6<7 and 7<6)
print(5<6 or 6<5)
print(not True)

edad=int(input("ingresa tú edad: "))
pasaporte=input("tiene pasaporte: ")
if edad>18 and pasaporte=="si":
    print("es mayor de edad y tiene pasaporte puede viajar")
elif edad>18 and pasaporte=="no":
    print("No puedes viajar")
elif edad<18 and pasaporte=="no":
    print("no puedes viajar")
if edad<18 and pasaporte=="si":
    print("si puede viajar, con tu acompañante")







