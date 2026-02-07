print("=" * 40)
print("MY CALCULATOR".center(40))
print("=" * 40)

print("Please select a type below.".center(40))
print("1) Addition".center(40))
print("2) Subtraction".center(40))
print("3) Multiply".center(40))
print("4) Division".center(40))
choice = input("Type (1/2/3/4): ")

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

if choice == "1":
    print("Answer:", num1 + num2) 
    
elif choice == "2": 
    print("Answer:", num1 - num2)

elif choice == "3": 
    print("Answer:", num1 * num2)

elif choice == "4":
    if num2 != 0:
        print("Answer:", num1 / num2)
    else:
        print("Cannot divide by zero! Try again!")

else:
    print("Invalid choice! Try again!")