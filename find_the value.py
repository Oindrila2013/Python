my_dict = {}
my_dict = {1: 10, 2: 20, 3: 30, 4: 40}

num = int(input("Enter a number key: "))

if num in my_dict:
    print("Value:", my_dict[num])
else:
    print("That number key doesn’t exist in this code, pls try another number key.")
