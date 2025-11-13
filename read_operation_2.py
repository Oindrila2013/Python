file = open("codingal.txt", "r")
print("Reading the first line.")
print(file.readline())
file.close()


file = open("codingal.txt", "r")
print("Reading the multiple lines.")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()


file = open("codingal.txt", "r")
print("Looping through the lines.")

for line in file:
    print(line)

file.close()