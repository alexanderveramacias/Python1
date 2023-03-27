if 6<7:
    pass
elif 7>6:
    pass
else:
    pass
#int(input("introduce el número perteneciente al día de la semana"))
día=int(input("introduce el número perteneciente al día de la semana: "))
if día==1:
    print("domingo")
elif día==2:
    print("lunes")
elif día==3:
    print("martes")
elif día==4:
    print("miercoles")
elif día==5:
    print("jueves")
elif día==6:
    print("viernes")
elif día==7:
    print("sábado")
else:
    print("el número no pertenece a un día de la semana")
número__1=int(input("ingresa un número: "))
número__2=int(input("ingresa otro número: "))
if número__1>número__2:
    print(f"{número__1} es mayor a {número__2}")
elif número__1<número__2:
    print(f"{número__2} es mayor a {número__1}")
else:
    print("el valor ingresado no es un número")

múltiplo__10=int(input("ingresa un número: "))
if múltiplo__10 % 10==0:
    print("el número ingresado es múltiplo de 10 ")
else:
    print("el número ingresado no es múltiplo de 10")

rel=int(input("introduce el número perteneciente al día de la semana: "))
if rel==1 or rel==2 or rel==3 or rel==4 or rel==5 or rel==6 or rel==7:
    print("el número ingresado si es un día de la semana")
if rel==1:
    print(not "es un día de la semana") 
if rel==2 and rel==3:
    print("el 2 y el 3 si son números de la semana")
else:
    print("no es un día de la semana")
nombre_1=input("ingrese un nombre")
if nombre_1!= "alex":
    print("este nombre no es válido")
else:
    print("bienvenido alex")







