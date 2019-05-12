class Animal:
    @property
    def terrestre(self):
        return True

class Felino(Animal):
    @property
    def garras_retractiles(self):
        return True

    def cazar(self):
        print("El felino esta cazando")

class Gato(Felino):
    def gato_cazador(self):
        self.cazar()

class Jaguar(Felino):
    pass  


gato = Gato()
juaguar = Jaguar()

print(gato.cazar())
print(juaguar.garras_retractiles)