class Cat: # our cat entity 
    # this is the constructor
    # it will create a cat for us in the code
    # we have said that to create a cat we need a given_name & given_colour
    def __init__(self,given_name,given_colour): # self is the CURRENT cat we are creating
        self.name = given_name
        self.colour = given_colour
        
# an instance is a specific occurence of a class
mimi = Cat("Mimi","Brown") # an instance of cat
print(mimi.name, mimi.colour)