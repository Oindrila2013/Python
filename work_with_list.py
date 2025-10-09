abc = ["Apple", "Banana", "Guava", "Mango", "Kiwi"]

print("lenght of list: ", len(abc))
print("First element of the list: ", abc[0])
print("Last element of the list: ", abc[-1])

abc.append("Papaya")
print("After appending Papaya to the list: ", abc)

abc.remove("Guava")
print("After removing the Guava from the list: ", abc)

abc.sort()
print("Sorted list: ", abc)

abc.pop(1)
print("After popping the element from the list: ", abc)

abc.reverse()
print("Reversed list: ", abc)

print("Multiplication of list: ", abc*2)

abc = abc[:4]
print("Sliced list: ", abc)

abc.clear()
print(abc)