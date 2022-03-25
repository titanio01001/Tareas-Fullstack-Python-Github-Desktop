print("¡Hola Mundo!")
variable="¡Hola Mundo!"
print(variable)

class Usuario:
    def __init__(self, name):
      self.name = name
    

    def myfunc(self):
      print("Hola " + self.name)

p1 = Usuario(input("Introduce tu nombre: "))
p1.myfunc() 

import math

x= ((3+2)/(2*5))**2
print(x)

class Usuario:
    def __init__(self, horas, costo):
      self.horas = horas
      self.costo = costo

    def myfunc(self):
      print(self.costo * self.horas)

p1 = Usuario(float(input("Introduce tus horas trabajadas: ")), float(input("Introduce el coste por hora trabajada: ")))
p1.myfunc() 

class n:
    def __init__(self, numero):
            self.numero = numero
    def myfunc(self):
        print(self.numero*((self.numero+1)/2))
        
n1= n(float(input("Introduce un numero entero positivo: ")))
n1.myfunc()


class IMC:
    def __init__(self, kg, m):
            self.kg = kg
            self.m = m
    def myfunc(self):
        print("Tu índice de masa corporal es " + str(round(self.kg/(self.m**2),2)))
        
IMC1= IMC(float(input("Introduce tu peso (kilogramos): ")), float(input("Introduce tu estatura (metros): ")))
IMC1.myfunc()
