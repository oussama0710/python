class Pet:
    def __init__(self, name , type , tricks,noise):
        self.name=name
        self.type=type
        self.tricks=tricks
        self.energy=75
        self.health=100
        self.noise=noise


    def sleep(self):
        self.energy+= 25
        return self


    def eat(self):
        self.energy+=5
        self.health+=10
        return self


    def play(self):
        self.health+=5
        return self


    def noise1(self):
        print(self.noise)
        return
    
class Ninja:
    def __init__(self, first_name , last_name , pet_food , pet ):
        self.first_name=first_name
        self.last_name=last_name
        self.pet_food=pet_food
        self.pet=pet
    def walk(self):
        self.pet.play()
    def feed(self):
        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f"Feeding {self.pet.name} {food}!")
            self.pet.eat()
        else:
            print("Unfortunately! there is no food")
        return self
        
    def bathe(self):
        self.pet.noise1()

    
# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
# feed() - feeds the ninja's pet invoking the pet eat() method
# bathe() - cleans the ninja's pet invoking the pet noise() method

my_pet_food = ['Pizza','Burger']

marwen = Pet("Mr Marwen","Horse","agressive","Hey Hey")

mohsen = Ninja("mohsen","jaafer",my_pet_food, marwen)

mohsen.feed()

mohsen.walk()
mohsen.bathe()
