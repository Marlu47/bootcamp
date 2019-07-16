class Persona: #creamos la clase persona, seria como una receta o un plano
    edad = 0

    def __init__ (self, un_nombre): #creamos los atributos (caracteristicas del objeto). metodo constructor
        self.mi_nombre = un_nombre # self es para referirse al objeto mismo 
        print("Hola naci, me llamo", self.mi_nombre)

    def cumple(self): #def es metodo cuando esta dentro de una clase(son las acciones que puede realizar el objeto)
        self.edad = self.edad + 1

pepe = Persona("pepito")
pepa = Persona("pepita")
print(pepe.edad)
print(pepe.mi_nombre)

for cumplir in range(6):
    pepe.cumple()
print(pepe.edad)
