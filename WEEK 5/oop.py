# Assignment 1 Designing my own class
class Superhero:
    def __init__(self, name, power, weakness, age):
        self.name = name
        self.power = power
        self.weakness = weakness
        self._age = age
    
    def intro(self):
        print(f"Hi, I am {self.name} and I am {self._age}")
    
    def get_power(self):
        print(f"Hi I am {self.name} and my power is {self.power}")
    
    def get_weakness(self):
        print(f"Hi I am {self.name} and my weakness is {self.weakness}")
    
    def get_age(self):
        return self._age
    
    def set_age(self, age):
        self._age = age
        print(f"Age of {self.name} isupdated to {self._age}")

superhero1 = Superhero("Superman","Strength","kryptonite", 27)
superhero2 = Superhero("Flash", "Speed", "Traps", 35)
superhero3 = Superhero("Wonderwoman", "Strength", "Magic", 34)
superhero4 = Superhero("Batman", "Intelligence", "Fear", 50)
superhero5 = Superhero("Hulk", "Strength", "Rage", 17)

superhero1.intro()
superhero4.get_power()
superhero5.get_weakness()


# Activity 2 Polymorphism Challenge

class Cow:
    def speak(self):
        return "Mooooo"

class Rooster:
    def speak(self):
        return "Cock-a-doodle-doo"

class Pig:
    def speak(self):
        return "Oink oink"

class Goat:
    def speak(self):
        return "Maaaa"

for Animal in [Cow, Rooster, Pig, Goat]:
    animal = Animal()
    print(animal.speak())