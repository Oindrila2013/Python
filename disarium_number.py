num = int(input("Enter a number: "))
sum = 0
temp = num
length = len(str(num))

while temp > 0:
    digit = temp % 10
    sum += digit ** length
    temp //= 10
    length -= 1

if sum == num:
    print(num, "is a Disarium number!")
else:
    print(num, "is not a Disarium number!")