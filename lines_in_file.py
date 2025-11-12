file = open("codingal.txt", "r")

count = 0

readfile = file.read()

coloist = readfile.split("\n")

for i in coloist:
    if i:
        count += 1

print("the number of lines in the file: ")
print(count)