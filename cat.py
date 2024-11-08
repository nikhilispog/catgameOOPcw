class Cat: # our cat entity 
    # this is the constructor
    # it will create a cat for us in the code
    # we have said that to create a cat we need a given_name & given_colour
    def __init__(self,given_name,given_colour): # self is the CURRENT cat we are creating
        self.name = given_name
        self.colour = given_colour
        self.age = 1 # additional hard-coded attributes
        self.energy = 50
        self.intelligence = 5
        self.weight = 5
    def train(self):
        print(f"{self.name} is training")
        self.intelligence +=1
        self.energy -=5
    def sleep(self):
        print(f"{self.name} is sleeping")
        self.energy +=10
    def eat(self):
        print(f"{self.name} is eating some good food")
        self.energy+=10
        self.weight+=2
    def pet(self):
        print(f"You pet {self.name} for a while")
        self.intelligence += 1
        self.energy -= 5
    def status(self):
        print("Name:",self.name)
        print("Colour:",self.colour)
        print("Age:",self.age)
        print("Energy:",self.energy)
        print("Intelligence:",self.intelligence)
        print("Weight:",self.weight)
   