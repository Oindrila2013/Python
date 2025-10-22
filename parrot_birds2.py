class parrot:

    def __init__(self, name, age):
        self.name = name 
        self.age = age
    
    def sing(self,song):
        return "{} is singing {}".format(self.name, song)
    
    def dancing(self):
        return "{} is dancing ".format(self.name)
    
blu = parrot("Blu", 10)

print(blu.sing("alone part 2"))
print(blu.dancing())