from cat import Cat

# an instance is a specific occurence of a class
mimi = Cat("Mimi","Brown") # an instance of cat
mimi.train()
print(mimi.name, mimi.colour)

asta = Cat("Asta","Black")
asta.sleep()
print("mimi",mimi.energy)
print("asta",asta.energy)