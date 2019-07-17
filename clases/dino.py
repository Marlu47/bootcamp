#lo que uno pone en el metodo consy=tructor es especifico para ese objeto, 
# no es para generalizar, por eso no lo ponemos en os atributos
# se le puede definir las variables de una vez con el objetivo
#none es una caja vacia donde podemos poner lo que queremos, puedo llenar o no llenar
#al poner = en los argumentos. toma ese valor. ej patas=2, sin especificar en la lista 
#una lista es para poner mas de un valor 
class Dino:
    ojos = 2
    def __init__(self, un_nombre, un_color, canti_patas=4, un_genero=None):
        self.nombre = un_nombre
        self.color = un_color
        self.patas = canti_patas
        self.genero = un_genero
        print("Naci")
        
    def saludar(self):
        print("hola me llamo", self.nombre, "tengo", self.patas, "patas y soy", self.color)
    
    def cortar_pata(self, cantidad_de_patas_a_cortar=1):
        self.patas = self.patas - cantidad_de_patas_a_cortar
    
    def decir_genero(self):
        print("hola soy", self.nombre, "y me identifico como", self.genero)

pepe = Dino ("kike", "verde", 4,"macho")
pepe.saludar() #cuando son acciones (metodos) siempre termina con parentesis
#cuando son atributos sin parentesis
# print(pepe.nombre) 
# print(pepe.color)
# print(pepe.patas)
# print(pepe.genero)
#print("hola me llamo",pepe.nombre, "soy de color", pepe.color,"tengo", pepe.patas, "patas y me identifico como", pepe.genero)
lilo = Dino ("lilodi", "rosa", 6, "hembra") #cada vez que creo un objeto tiene todas las caracteristicas y
# puede realizar todas las acciones de la clase Dino
lilo.saludar()

rosa = Dino ("rosita", "purpura", 4, "hembra")
rosa.saludar()
rosa.cortar_pata()
rosa.saludar()

class TRex(Dino):
    def __init__(self, nombre, patas=4, color=None):
        self.nombre = nombre
        self.patas = patas
        self.color = color
        print("hola soy un TRex y me llamo", self.nombre)

robert = TRex("Roberto el TRex")
print(robert.ojos)
robert.saludar()
robert.decir_genero()



