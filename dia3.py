'''ing_pan=["harina","levadura","sal","azucar","agua"]
def imprimir_lista (ingredientes,nombre_producto):
    print("lista de compras de", nombre_producto)
    print("____________________")
    for producto in ingredientes:
        print(producto)

imprimir_lista(ing_pan, "pan")
ing_salsa=["tomate","azucar", "sal","cebolla"]
imprimir_lista(ing_salsa, "salsa de pizza")

#condicionales
# el if siempre es una pregunta con una condicional 
#el operador sino es else
#identacion: es la tabulacion 
#cuando se hace una pregunta o condicion poner == (es igual), no solo un= porque es de programacion
# == igual
#!: distitnto o no igual 

a=3
#pregunta
if a > 3:
    print("si, a es mayor a 3")
    print("chau!")
else:
    print("no, a no es mayor a 3")
#pregungta2
if a == 3:
    print("a es igual a 3")
nota=60
#pregunta3
if nota >= 60:
    print("pasasteeee!!!")
else:
    print("hule yaa")

#eje. crear una funcion que reciba como parametro 
#una nota del 1 al 100 e imprima si pasaste o te aplasaste(se aprueba con 61)
nota=55
def prueba(nivel):
    if nivel > 60:
        print("pasaste")
    else: 
        print("no pasaste")
prueba(nota)
 
#el and es para anadir una condicion-pregunta mas, en donde todas se deben cumplir o ser verdad 
a=7
if a > 5 and a < 10:
    print("a es mayor a 5 y menor que 10")
else:
    print("a no esta en el rango, alguna de las 2 condiciones no se cumplieron")

if a > 5 or a < 10:
    print("a es mayor que 5 o menor que 10")
else:
    print("a no es mayor que 5 ni menor que 10")


# or hace que pueda cumplir una de las condiciones 
# si yo hago print de una comparacion me va a dar verdadero o falso . true or false, o es igual 
# false tipo de dato que sirve para comparar 
# elif es para hacer varias preguntas 
# elif, if, else es un operador asi como for 
# else es el sino 

edad=7
if edad > 18:
    print("dberia estar en la universidad")
elif edad > 13:
    print("deberia estar en la secundaria")
elif edad > 6:
    print("deberia estar en la primaria")
else:
    print("deberia estar en su casa bbdlc")

#ej: crear una funcion puntaje que reciba como parametro una nota 
#del 1 al 100 e imprimir que nota sacaste
#nota <60----->1
#nota entre 60 y 70 ----->2
#nota entre 71 y 75----->3
#nota entre 76 y 85------>4
#nota mayor que 85 ------>5 
note=90
def puntaje(nota):
    if nota <=60:
        print("tu nota es 1")
    elif nota >= 60 and nota <= 70:
        print("tu nota es 2")
    elif nota >70 and nota < 75:
        print("tu nota es 3")
    elif nota >76 and nota < 85:
        print("tu nota es 4")
    elif nota >= 85:
        print("tu nota es 5")
puntaje(note) #la llamada
#booleano: false y true 
#int es para comvertir string en enteros-numeros y str  para convertir en int 
#imput es el que te permite ingresar por teclado el valor 

#ej1: pedir al usuario que ingrese tres numeros y multiplicarlos 
#entre si, imprimir el resultado

#numero1= input("ingresa los numeros:")
#numero2= input("ingresa los numeros:")
#numero3= input ("ingresa los numeros:")
#print(int(numero1)*int(numero2)*int(numero3)) #una vez hecho todo esto pulsar enter

#ej2: pedir al usuario un numero del 1 al 100 y llamar a la 
#funcion  que retornaba la nota que creamos hace rato 
#utilizando  el valor ingresando por el usuario
# con input pedis y te trae en texto-str por lo tanto cuando necesitamos un int hay que convertir 
#para comentar algo grande poner tres comillas abajo y tres arriba 

num= input("numero:")
puntaje(int(num))

#bucle while= mientras 
#se van a ejecutar las cosas mientras se cumple la condicion para eso sirve while
#crt+barra para poner todo de una como comentario 
#el contador es como que va sumando o restando de acuerdo a lo que queremos
#  hasta llegar al limite que nosotros determinamos 

x=0
while x != 5: #mientras x sea distitnto a 5
    print("hola esto es un bucle while mientras x sea distito de 5")  
    x= int(input("ingresa un numero:"))  #ingresamos un valor para x
    print("el valor de x ahora es", x)
print("termino!!!")

#contador inverso
contador = 10
while contador >0:
    print("sigo en el bucle while")
    contador = contador - 1
    print("te quedan", contador,"oportunidades")
print("termino")
#contador 
contador=10 #inicializar la variable
while contador < 20:
    print("sigo en el bucle while")
    contador = contador + 1
'''
#usando while pedir al usuario 5 ingredinetes para hacer pizza
# y agregar a una lista, al final imprimir la lista 
#pedir al usuario es input
ingr=0
pizza=[]
while ingr < 5:
    ingrediente=input("ingresar ingredientes ")
    pizza.append(ingrediente)
    ingr = ingr + 1
print("esta mi pizza", pizza)

adivino = False 
numero_secreto = 7

while adivino == False:
    apuesta = input("adivina el numero secreto del 1 al 10: ")

    if int(apuesta) == numero_secreto:
        print("GANASTEE!!")
        adivino = True
    else:
        print("segui participando nde arruinado")




#ej4 crear un juego de adivinar el numero como el de arriba 
#darle pista al usuario si el numero que ingreso es mayor o menor 
#al numero a adivinar 
#pista usar elif 

adivinar = False # esto se una para la condicion de entrada al while
numero_secreto = 40
intento=10

while adivinar == False and intento > 0:
    apuesta = input("Adivina el numero secreto del 1 al 100")
    if numero_secreto == apuesta:
        print("Adivinaaastee baby!!!")
    elif numero_secreto > apuesta:
        print("intenta un numero menor")
    elif numero_secreto < apuesta:
        print("intenta un numero mayor")
    

