print("=" * 40)
print("MY CALCULATOR".center(40))
print("=" * 40)

print("Please select a type below.".center(40))
print("1) Add".center(40))
print("2. Multiply".center(40))
choice = input("Type (1/2): ")

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

if choice == "1":
    print("Answer:", num1 + num2) 
    
elif choice == "2": 
    print("Answer:", num1 * num2)

else:
    print("Invalid choice")