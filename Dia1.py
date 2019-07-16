print(4*5) # print es una funcion para mostrar en pantalla 
print("hola mundo") # cadena de texto o strings
print("psicologia") # ejecutar archico de python en la terminal o ctrl f5
print("hola"*20) #cuando es texto hace falta poner comillas
print("con amor"*50) #poner espacios antes de la comilla en el inicio, y antes de que se cierre la comilla para que no salga juntos
#variables lugar donde guardas un valor, en donde se tiene almacenar un tipo de dato. el valor de la variable puede cambiar de acuerdo a lo que cada uno ponga
a=3
b=5
b=6 #siempre va cambiando el valor de acuerdo a lo que vas poniendo ultimamente 
print(a+b)
#si ven una coma en algun lugar es para separar elementos
print("hello",6) # al poner entre comas si puede unir numeros y textos
#ejercicios, crear una variable nombre y una variable edad, con sus datos e imprimir 
#hola, me llamo... y tengo...años
nombre="marlu" #utilizar las comillas para los textos en las variables
edad=25
profesion="psicologa"
hobby="leer"
print("hola, me llamo" ,nombre, "y tengo",edad, "años,y soy",profesion, "y mi hobby es",hobby)
#en las variables no es necesario utilizar + para unir a los otros textos, solo entre comas
lista_vacia=[]
#cuando vos pasas una variable, en realidad estas pasando el contenido de la variable
#al usar corchete en python se sabe que es una lista
#se llama indice a lo que esta en el corchete y siempre los elementos arrancan con 0 
listax=[1,2,3]
#ej. crear una lista datos que en el primer lugar este tu nombre 
#y en la segunda posicion este tu edad
#imprimir "hola me llamo...,y tengo ..años"
datos=["Marlu",25]
print("hola me llamo",datos[0],"y tengo",datos[1],"años")
#podes utilizar uno de los elementos de la lista, poniendo el nombre, y el numero del elemento en corchete
datos[1]=20
print("hola me llamo",datos[0],"y tengo",datos[1],"años") 
#para cambiar uno de los elementos, solo poner por ejemplo: datos[2]=20 (el valor que queremos que tenga)
#para ejecutar solo la linea nueva que hicimos :shift-enter
#para agregar algo o accionar en la lista, se pone el nombre de la lista seguido de .append ej:datos.append
#tarea: agregar una profesion y un hobby a la lsita datos previamente creada
datos.append("psicologa")
print(datos[2])
datos.append("hacer ejercicios")
print(datos[3])
print("hola me llamo",datos[0],"y tengo",datos[1],"años soy",datos[2],"y mi hobby es",datos[3] )
#para eliminar elementos de una lista hacer ej:datos.pop()
datos.pop()
print(datos)
#funcion len()= lenght que sinifica dimension o longitud
#la coma dentro de las comillas es una coma normal, pero fuera es oara separar una lista o variable 
print(len(datos))
saludo="hola, que tal"
print(saludo)
print(len(saludo))
#tarea: obtener la dimension de la lista datos e imprimir: la lista datos tiene... elementos"
print("la lista de datos tiene",len(datos),"elementos")
#imprimir el ultimo elemento de una lista sin saber cuantos elementos tiene
dimension=[1,2,3,6,7,8,9,0,8,7,5,3,4,5,6,7,8,9,7]
indicefinal= len(dimension)-1
print(dimension[indicefinal])
#la cantidad obtenida por len menos uno. para saber la cantidad del ultimo . lo conviertes el variable 
#bucles/loops/cilos/interacciones , sirve para hacer varias veces una accion 
lista_temas=["variables","lista","tipos de datos"]
for concepto in lista_temas:
    print("hoy aprendí", concepto)
    print("que gusto")
print("esto aprendi hoy")

#recorrer un lista con for e imprimir en cada ciclo 
#el valor del elemento con 3 signos de admiracion y al final 
#fuera del bucle "FIN!!!"
#ej: variables!!!
lista_larga=["emociones","sentimientos","pensamientos"]
for factores in lista_larga:
    print(factores,"!!!")
print("FIN!!!")

nombre_lista=["Mery","Naty","Abi","Sofi"]
for recado in nombre_lista:
    print("Feliz cumpleaños",recado)
print("Disfruta!!")

#range : para repetir palabras, puede hacerse tambien desde cierto numero eje: del 95 al 100. 
for x in range(10):
    print("HOLA",x)
 
 #ej imprimir los numeros del 1 al 100 usando for y range 
#imprimir el numero de resultado de la suma de los numeros del 1 al 10   
for numero in range(1,101):
    print("dormir",numero)

