class parrot:

    #class attribute
    species = "bird"

    #instance attribute

    def __init__(self, name, age):
        self.name = name 
        self.age = age

#creating instance
blu = parrot("Blu",10)
mac = parrot("Mac",5)

print("Blu is a {}".format(blu.species))
print("Mac is also a{}".format(mac.species))

print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(mac.name, mac.age))