#tipo de dato string/cadena de texto/str de texto
"esto es un string"
#tipo de dato intenger/entero/int
105 #tipo de dato entero
#listas 
[#listas vacias
#variables
#el nombre de la variable no acepta espacios
# con = asignabamos valor a la variable 
#al guardar numeros con comillas no hace la operacion, al contrario al guardar solo si lo hace 
#ej: 30+3 , "30+3"
varible_lista=["hola", nombre, 99]
#acceder a un elemnto de la lista, por la posicion
print(variable_lista[0]), edad, variable_lista[2]
#acciones/operaciones sobre listas
#a pop no le pones nada adentro de la parentesis, porque siempre elimina el ultimo elemento de la lista. 
variable_lista.append #agregar elemnto
variable_lista.pop()#eliminar el ultimo
variable_lista[2]=50 #para modificar el valor del elemento de la lista 
print(variable_lista)
#el for recorre una lista o un rango 
for loquesea in variable_lista:
    print(loquesea)
#len lo que hace es dar la dimension o longitud de la lsita 
len(variable_lista)
#imprimir los nueros del 1 al 10 
for cualquiercosa in range(10):
    print(cualquiercosa)
#el tamaño de la lista menos uno soempre va a ser el ultimo en la lista 
#poner +1 o 1,11
#elementos tiene, solucion general 
#lo que viene entre corchete es el indice
otra_lista=[5,"hola que tal","chau",4]
otra_lista.append("AAAA")

#solucion paso por paso
dim_lista=len(otra_lista)
print("la dimension de otra lista es", dim_lista)
indice_del_ultimo= dim_lista -1
print("el indice del ultimo elemenyo es", indice_del_ultimo)
print(otra_lista[indice_del_ultimo])

#solucion de una linea 
print(otra_lista[len(otra_lista)-1])

#estas dos formas son equivalentes
for numero in range(1,11):
    print(numero)
#a esto
for numero in [1,2,3,4,5,6,7,8,9,10]:
    print(numero)

#imprimir hola 10 veces
for numero in [1,2,3,4,5,6,7,8,9,10]:
    print("hola",numero) #imprimier numero es opcional 

#imprimir el numero de resultado de la suma de los numeros del 1 al 10 
changelle=[1,2,3,4,5,6,7,8,9,10] #se crea una lista 
a=0  #se crea una variable 
for x in challenge: #se crea un hilo que va a correr la lista
    a=a+x #se va acumulamdo 
    print(a)

    sumatoria=0
    for valor in range(1,11):
        sumatoria=sumatoria+valor
print(a)

#funciones
 
def nombre_de_la_funcion(argumentos):
    acciones #print

 suma(num1, num2):
    resultado= num1+num2
    return num1+num2

#equivalente a la de arriba
 suma2(num1, num2):
    return num1+num2

print(suma(5,10))
reult=suma(5,8)
print(resul)

#crear una funcion resta, que recoba como parametro dos numeros y retorne la resta de esos numeros 
#luego llamar a la funcion ew imprimir  el resultado 
def resta(n1,n2):
    print(n1-n2)
    return n1-n2 #return corta todo, interrumpe la ejecucion 
    print("chau")

resul=resta(4,2) #todo lo que esta en return se reemplaza en el llamado, 
#y es necesario guardar en una variable
print("el resultado es",resul)

#return te lanza el resultado y print imprime 

#crear una funcion saludo2 que reciba como parametro nombre y edad 
#e imprimir "hola spy...y tengo...años"
#llamar varias veces a la funcion con distitntos valores
#nota: retornar algo es opcional 

def saludo2(nombre,edad):
    return nombre,edad
print("hola soy",("Marlu"),"y tengo",(25),"años")

#otra opcion mejorada
#return normalmente para retornar un resultado u operacion 

def saludos(nombre,edad):
  print("hola me llamo",(nombre),"y tengo",(edad),"años") #no es necesario poner entre parentesis 
saludos("marlu",25)
saludos("will",22)
#al hacer el llamdo recien le das valor o argumentos
#  eje: a la saludos al hacer el llamado recien le di valor 
#ej: crear una funcion suma_lista que reciba como argumento una lista de numero
# y retorne la suma de sus elemntos 
#pistas: usar for y una variable 
listita=[1,2,3,4,5,6,7,8]
b=0
for c in listita:
    b=b+c
print(b)


sumatoria=0
for valor in range(1,11):
    sumatoria=sumatoria+valor
lis = [1,2,3,4]
#otra forma
def suma(numeros):
    sumatoria=0
    for valor in numeros:
        sumatoria=sumatoria+valor
    return sumatoria
print(suma(lis))
print(suma([1,2,3])) #tengo que poner en corchete cuando le estoy pasando un valor-lista que va a recorrer la variable

#ej2: lista al cuadrado 
#crear una funcion que reciba una lista de numero como parametro 
#y retorne una lista con los numeros al cuadrado
#lista_cuadrado(listita): [1,4,9,16,25]

def lista_num(number):
    c=[]
    for elvalor in number:
        c.append(elvalor*elvalor)
    return c
print(lista_num([1,2,3,4]))

#con return podemos utilizar el dato en otra operacion cosa que con print no podemos hacer
#se puede haacer un for, dentro de otro for, por ejemplo haciendo pop, con range
#ej3: eliminar todos los elementos de una lista utilizando "for"
grupo5=["n","f1","f2","a"]
print("antes", grupo5)
for j in grupo5: #el for recorre la lista desde el el primer elemento
    grupo5.pop()
print("despues", grupo5)
#version acertada
for j in range(len(grupo5)):
    grupo5.pop()

#crear una funcion suma_cuadrado que reciba una lista de numeros
#y retorne el valor de la suma de cada numero al cuadrado 
#[1,2,3]-- 1+4+9--14
talis=[1,2,3]

print(listita(lista_num(talis))) #hice una funcion dentro de una funcion en otra funcion
# utilice los datos que ya tenia anteriormente gracias a return
#los datos son los resutados de las operaciones de suma y los cudrados de los ejercicios anteriores 



