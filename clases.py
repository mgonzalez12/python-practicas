class Lapiz:
    color = 'Amarillo'
    contiene_borrador = False
    usa_grafito = True

    def dibujar(self):
        print("el lapiz esta dibujado")

    def borrar(self):
        print("Borrando")

lapiz_generico = Lapiz()
lapiz_generico.dibujar()     