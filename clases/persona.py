class Persona: #creamos o definimos la clase persona, 
    #se crea un objeto, nombre de la clase, instanciar: es crear un objeto unico 
    #seria como una receta o un plano, para crear un objeto
    #todo lo que esta en la clase es lo que va a crear el objeto, es el molde(clase)
    edad = 0 #es un atributo de clase o propiedad, serian las caracteristicas 
    nacionalidad = " " #son variables que estan dentro de una clase, los atributos.
#metodos son las acciones que podemos realizar con los objetos
    def __init__ (self, un_nombre): #creamos los atributos (caracteristicas del objeto). 
        #metodo constructor, que construye el objeto
        self.mi_nombre = un_nombre # self es para referirse al objeto mismo 
        print("Hola naci, me llamo", self.mi_nombre) 
        #los metodos son funciones dentro de una clase

    def cumple(self): #def es metodo cuando esta dentro de una clase(son las acciones que puede realizar el objeto)
        self.edad = self.edad + 1 #que aumenta la propiedad edad en 1

    def asignar_edad(self, una_edad): #asignar edad es un metodo que recibe un argumento 
        #y asigna a la propiedad  edad del objeto 
        self.edad = una_edad
    
    def nac(self, una_nacio):
        self.nacionalidad = una_nacio


    

pepe = Persona("pepito") #pepe es un objeto de la clase persona 
pepa = Persona("pepita")
mujer = Persona("Marlu")
print(mujer.edad)
print("soy ",mujer.mi_nombre," y tengo", mujer.edad, "y mi nacionalidad es", mujer.nacionalidad)
print(pepe.edad)
print(pepe.mi_nombre)
mujer.nac("paraguaya")
print("hola soy", mujer.mi_nombre, "y mi nacionalidad es", mujer.nacionalidad )

# for cumplir in range(6):
#     pepe.cumple()
# print(pepe.edad)

#ejer: agregar un metodo en la clase persona que asigne nacionalidad
#y otro metodo saludar que imprima "hola soy nombre y mi nacionalidad es"

# hacer una clase que se llama vehiculo que tenga tres atributos 
# y uno que sea cantidad_ruedas, y un metodo que sea definir _tipo 
# que me diga si es "bicicleta, triciclo,auto" de acuerdo a ala cantidad de ruedas


class Vehiculo:
    ruedas = 0
    color = ""
    modelo = ""
    
    def __init__(self, cantidad_ruedas): #se pueden pasar todos los atributos (variables)
        self.ruedas = cantidad_ruedas
    
    def col(self, un_color):
        self.color = un_color



