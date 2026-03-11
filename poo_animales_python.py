class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def hacer_sonido(self):
        print("El animal hace un sonido.")

    def mostrar_info(self):
        print(f"Nombre: {self.nombre} | Especie: {self.especie}")

class Perro(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} está ladrando: ¡Guau Guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} está maullando: ¡Miau Miau!")

class Vaca(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} está mujiendo: ¡Muuuu!")

class Pajaro(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} está cantando: ¡Pío Pío!")

class Leon(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} está rugiendo: ¡Roaaar!")

class Oveja(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} está balando: ¡Beee Beee!")

class Cerdo(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} está gruñendo: ¡Oink Oink!")

class Pato(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} está graznando: ¡Cuac Cuac!")

class Conejo(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} está chillando: ¡Cuiii Cuiii!")

class Gallina(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} está cacarreando: ¡Co Co Coo!")

animales = [
    Perro("Rex", "Canis lupus familiaris"),
    Gato("Michi", "Felis catus"),
    Vaca("Lola", "Bos taurus"),
    Pajaro("Perico", "Melopsittacus undulatus"),
    Leon("Simba", "Panthera leo"),
    Oveja("Dolly", "Ovis aries"),
    Cerdo("Puerquito", "Sus scrofa domesticus"),
    Pato("Donald", "Anas platyrhynchos"),
    Conejo("Bugs", "Oryctolagus cuniculus"),
    Gallina("Pollita", "Gallus gallus domesticus")
]

print("====== Animales =====")
for animal in animales:
    animal.mostrar_info()
    animal.hacer_sonido()
    print("---")