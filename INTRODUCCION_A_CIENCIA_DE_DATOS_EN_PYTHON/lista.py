familiares=["alex","sara","sandra","elkin","daniel","consuelo","beatriz","fernando","kevin"]
for nombre_de_familiar in familiares:
    #print(nombre_de_familiar+" "+"estos son mis familiares")
    if nombre_de_familiar == "daniel": 
        print(f"{nombre_de_familiar} este es mi hijo")
    elif nombre_de_familiar == "sara":
        print(f"{nombre_de_familiar} esta es mi hija")

# hacer una lista de frutas e iterarlas con un bucle for, luego cuando encuentre la fruta manzana e imprima manzana en mayuscula sin tener que modificar el dato original.
# hacer una lista con los dias de la semana e imprimipir la cantidad de dias que hay.

frutas=["arandano","banano","manzana","pera","piña","durazno","papaya","melon","mango","marañon","kiwi","patilla","uchuva","grosella"]
for manzana_en_mayuscula in frutas:
    if manzana_en_mayuscula == "manzana":
        print(f"{manzana_en_mayuscula.upper()}")

semana=["domingo","lunes","martes","miercoles","jueves","viernes","sabado"]
#for dia_de_la_semana in semana:
#    print(f"{(dia_de_la_semana)}")
print(len(semana))

# métodos
variable=[]
variable.append(9)
variable.append("alex")
print(f"{len(variable)}")

variable.remove("alex")
variable.remove(9)

variable.append("alexander")
variable.append(9)
variable.append(True)
popv=variable.pop()
print(popv)

variable.append("daniel")
variable.append("alexander")
variable.append("pedro")
variable.append("pablo")
variable.append("juan")
variable.remove(9)
variable.remove("alexander")
variable.reverse()
#variable.sort(reverse=True)
print(variable)
