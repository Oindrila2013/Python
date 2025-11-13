file = open("codingal.txt", "r")
print(file.read())
file.close()

file = open("codingal.txt", "r")
print("Opening the first 15 characters.")
print(file.read(15))
file.close()