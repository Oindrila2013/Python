file = open("codingal1.txt", "r") 

print(file.read())

file.close()


file = open("codingal1.txt", "w")

file.write("Hello, this is Ankita. I am a student of codingal")

file.close()


file = open("codingal1.txt", "a")

file.write("I love learning coding. It is so much fun.")

file.close()