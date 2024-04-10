class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        return self.sound

class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name, "Woof")

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name, "Chirp")

class Reptile(Animal):
    def __init__(self, name):
        super().__init__(name, "Hiss")

# Create instances of each animal
mammal = Mammal("Dog")
bird = Bird("Parrot")
reptile = Reptile("Snake")

# Print the sound each animal makes
print(f"{mammal.name} says {mammal.make_sound()}")
print(f"{bird.name} says {bird.make_sound()}")
print(f"{reptile.name} says {reptile.make_sound()}")