# empty dictionaries

my_dict = {}

# ditionaries with integer values

my_dict ={ 1 : "Apple" , 2 : "ball"}

# dictionaries with mixed keys

my_dict = {"name": "Jack", 1 : [1,2,4,5]}
my_dict = {"name": "Jack", "age": 27}

# get the items

print(my_dict["name"])
print(my_dict.get("age"))

# update the values

my_dict["age"] = 30
print(my_dict)

# add items

my_dict["Gender"] = "Male"
print(my_dict)

# remove element

my_dict.pop("age")
print(my_dict)

# removbe all elements
my_dict.clear()