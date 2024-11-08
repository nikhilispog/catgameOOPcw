from cat import Cat

# an instance is a specific occurence of a class

catname = input("What would you like to name your cat?")
catcolour = input("What is the colour of your cat?")
cat1 = Cat(catname,catcolour) # a new instance of cat
cat1.sleep()
cat1.eat()
cat1.status()

while True:
    action = input("What would you like to do?")
    if action == "sleep":
        cat1.sleep()
    elif action == "eat":
        cat1.eat()
    elif action == "status":
        cat1.status()