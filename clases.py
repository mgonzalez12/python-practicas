class Lapiz:
    def __init__(self,color,contiene_borrador,usa_grafito, *args, **kwargs):
        self.__color = color
        self.contiene_borrador = contiene_borrador
        self.usa_grafito = usa_grafito

    def dibujar(self):
        print("el lapiz esta dibujado")

    def borrar(self):
        print("Borrando")

lapiz_generico = Lapiz("verde", True,True)
lapiz_generico.dibujar()     

