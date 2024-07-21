class Animal:

    def __init__(self,edad,color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("El animal acaba de nacer")
    

class Pajaro(Animal):
    def __init__(self, edad, color,especie):
        super().__init__(edad, color)
        self.especie = especie

piolin = Pajaro(2,"Amarillo","Pajaro amarillo")
piolin.nacer()
